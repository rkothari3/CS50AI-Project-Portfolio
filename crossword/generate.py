import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        # Create a 2D list initialized with None
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        
        # Iterate over each variable and its assigned word in the assignment
        for variable, word in assignment.items():
            direction = variable.direction  # Get the direction of the variable (ACROSS or DOWN)
            
            # Place each letter of the word in the correct position in the grid
            for k in range(len(word)):
                # Calculate the row index
                i = variable.i + (k if direction == Variable.DOWN else 0)
                # Calculate the column index
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                # Assign the letter to the correct position in the grid
                letters[i][j] = word[k]
        
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             (rect[0][1] + ((interior_size - h) / 2) - 10)),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for var in self.domains:
            var_len = var.length
            to_remove = set() # Create a set to store the values to remove

            for val in self.domains[var]:
                if len(val) != var_len:
                    to_remove.add(val)
        # Remove the values that are inconsistent with the variable's length
        self.domains[var] -= to_remove

    def revise(self, x, y): # x and y are variables
        """
        - x and y will both be Variable objects representing variables in the puzzle.
        - x is arc consistent with y when every value in the domain of x has a possible value in the domain of y that does not cause a conflict.
        - A conflict in the context of the crossword puzzle is a square for which two variables disagree on what character value it should take on.
        - To make x arc consistent with y, remove any value from the domain of x that does not have a corresponding possible value in the domain of y.
        - Access self.crossword.overlaps to get the overlap, if any, between two variables.
        - The domain of y should be left unmodified.
        - The function should return True if a revision was made to the domain of x; it should return False if no revision was made.
        """
        # Switch
        revised = False

        # Get the overlap between the two variables
        # Returns None if the variables do not overlap
        # Otherwise, returns a tuple (i, j) where i is the index of the character in x that overlaps with the character in y
        overlap = self.crossword.overlaps[x, y] 
        
        if overlap is None:
            return False
        
        # Check each value in x's domain
        to_remove = set()
        for x_val in self.domains[x]:
            # Get the overlapping character for x_val
            if overlap[0] < len(x_val):
                x_char = x_val[overlap[0]]
                
                # Check if there's any compatible value in y's domain
                has_compatible = False
                for y_val in self.domains[y]:
                    if overlap[1] < len(y_val) and x_char == y_val[overlap[1]]:
                        has_compatible = True
                        break
            else:
                has_compatible = False
                    
            # If no compatible value found, mark for removal
            if not has_compatible:
                to_remove.add(x_val)
                revised = True
        
        # Remove incompatible values from x's domain
        self.domains[x] -= to_remove
        return revised

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # Initialize the queue with all the arcs in the problem
        if arcs is None:
            queue = [] # Everything we need to make arc consistent.
            for x in self.domains:
                for y in self.domains:
                    if x != y: # Avoid adding the same variable twice
                        queue.append((x, y))
        else:
            queue = arcs.copy() # Use .copy() to avoid modifying the original list
        
        # While queue is non-empty:
        while queue: # True when not empty; false when empty
            (x, y) = queue.pop(0) # Remove the first element from the queue
            
            # If revision is made to x's domain
            if self.revise(x, y): # Refering to the revise method in this class
                # if x's domain is empty, return False
                if len(self.domains[x]) == 0:
                    return False
                # Add new arcs to queue
                # For each neighbor of x (except y)
                for z in self.crossword.neighbors(x) - {y}:
                    queue.append((z, x))
        return True

    def assignment_complete(self, assignment):
        """
        The assignment_complete function should check if a given assignment is complete.

        - An assignment is a dictionary where the keys are Variable objects and the values are strings representing the words those variables will take on.
        - An assignment is complete if every crossword variable is assigned to a value (regardless of what that value is).
        - The function should return True if the assignment is complete and return False otherwise.
        """
        # Iterate over each variable in the crossword
        for var in self.domains:
            if var not in assignment:
                return False
        # If all variables in the assignment, return True, meaning the assignment is complete
        return True 

    def consistent(self, assignment):
        """
        The consistent function should check to see if a given assignment is consistent.

        - An assignment is a dictionary where the keys are Variable objects and the values are strings representing the words those variables will take on. Note that the assignment may not be complete: not all variables will necessarily be present in the assignment.
        - An assignment is consistent if it satisfies all of the constraints of the problem:
            - All values are distinct.
            - Every value is the correct length.
            - There are no conflicts between neighboring variables.
        - The function should return True if the assignment is consistent and return False otherwise.
        """
        usedVars = []

        for var_X in assignment: # Iterating over keys
            val_X = assignment[var_X] # Getting the value of the key

            # if the assigned word is alr used, not consistent
            # (All values are distinct)
            if val_X in usedVars:
                return False
            else:
                usedVars.append(val_X)

            # Check if variable's value has the correct length
            # (Every value is the correct length)
            if len(val_X) != var_X.length:
                return False
            
            # Check for conflicts between neighboring variables
            for var_Y in self.crossword.neighbors(var_X):
                if var_Y in assignment:
                    val_Y = assignment[var_Y]
                    overlap = self.crossword.overlaps[var_X, var_Y]
                    if overlap is not None and val_X[overlap[0]] != val_Y[overlap[1]]:
                        return False
        # Otherwise, all assignments are consistent
        return True
    
    def order_domain_values(self, var, assignment):
        """
        The order_domain_values function should return a list of all of the values in the domain of var, ordered according to the least-constraining values heuristic.

        - var will be a Variable object, representing a variable in the puzzle.
        - The least-constraining values heuristic is computed as the number of values ruled out for neighboring unassigned variables.
        - If assigning var to a particular value results in eliminating n possible choices for neighboring variables, order your results in ascending order of n.
        - Any variable present in assignment already has a value and shouldn’t be counted when computing the number of values ruled out for neighboring unassigned variables.
        - For domain values that eliminate the same number of possible choices for neighboring variables, any ordering is acceptable.
        - Access self.crossword.overlaps to get the overlap, if any, between two variables.
        - It may be helpful to first implement this function by returning a list of values in any arbitrary order (which should still generate correct crossword puzzles). Once your algorithm is working, you can then go back and ensure that the values are returned in the correct order.
        - You may find it helpful to sort a list according to a particular key: Python contains some helpful functions for achieving this.
        """
        # Create a dictionary to store the number of constraints for each value in the domain
        constraints = {}

        # Get variables' domain values
        for value in self.domains[var]:
            count = 0 # Keeps track of count, refreshes for each iteration

            # Check each neighbor of the variable
            for neighbor in self.crossword.neighbors(var):
                if neighbor not in assignment:
                    # Get the overlap between the variables
                    i, j = self.crossword.overlaps[var, neighbor]
                    # Count eliminated values for neighbor
                    for neighbor_val in self.domains[neighbor]:
                        if value[i] != neighbor_val[j]:
                            count += 1
            # Store the number of constraints for the value
            constraints[value] = count
        # Return sorted values based on constraints
        return sorted(constraints.keys(), key=lambda x: constraints[x])      

    def select_unassigned_variable(self, assignment):
        """
        The select_unassigned_variable function should return a single variable in the crossword puzzle that is not yet assigned by assignment, according to the minimum remaining value heuristic and then the degree heuristic.

        - An assignment is a dictionary where the keys are Variable objects and the values are strings representing the words those variables will take on.
        - You may assume that the assignment will not be complete: not all variables will be present in the assignment.
        - Your function should return a Variable object.
        - You should return the variable with the fewest number of remaining values in its domain.
        - If there is a tie between variables, you should choose among whichever among those variables has the largest degree (has the most neighbors).
        - If there is a tie in both cases, you may choose arbitrarily among tied variables.
        - It may be helpful to first implement this function by returning any arbitrary unassigned variable (which should still generate correct crossword puzzles). Once your algorithm is working, you can then go back and ensure that you are returning a variable according to the heuristics.
        - You may find it helpful to sort a list according to a particular key: Python contains some helpful functions for achieving this.
        """
        # Iterate over the variables in the crossword and remove the assigned variables to get the unassigned variables
        unassigned_vars = []
        for var in self.domains:
            if var not in assignment:
                unassigned_vars.append(var)

        # If there are no unassigned variables, return None
        if not unassigned_vars:
            return None

        # Find variable with minimum remaining values
        min_remaining_values = float('inf')  # Start with infinity
        min_vars = []  # List to store variables with minimum values

        for var in unassigned_vars:
            num_values = len(self.domains[var])
            if num_values < min_remaining_values:
                min_remaining_values = num_values
                min_vars = [var]
            elif num_values == min_remaining_values:
                min_vars.append(var)
        # Break ties using the degree heuristic
        # Degree heuristic: Choose the variable with the most neighbors
        # if min_vars has only one variable, return it
        if len(min_vars) == 1:
            return min_vars[0]
        else: # If there are multiple variables with the same number of remaining values
            max_degree = -1
            selected_var = None
            for var in min_vars:
                degree = len(self.crossword.neighbors(var))
                if degree > max_degree:
                    max_degree = degree
                    selected_var = var
            return selected_var

    def backtrack(self, assignment):
        """
        The backtrack function should:
        - Accept a partial assignment as input.
        - Use backtracking search to return a complete satisfactory assignment of variables to values if possible.

        An assignment is a dictionary where:
        - Keys are Variable objects.
        - Values are strings representing the words those variables will take on.
        
        The input assignment may not be complete (not all variables will necessarily have values).

        If it is possible to generate a satisfactory crossword puzzle, the function should:
        - Return the complete assignment: a dictionary where each variable is a key and the value is the word that the variable should take on.

        If no satisfying assignment is possible, the function should:
        - Return None.

        The algorithm may be more efficient if:
        - Search is interleaved with inference (e.g., maintaining arc consistency every time a new assignment is made).
        
        Note:
        - This is optional but permitted, as long as the function produces correct results.
        - The ac3 function allows an arcs argument in case you’d like to start with a different queue of arcs.
        """
        # If assignment is complete, return it
        if self.assignment_complete(assignment):
            return assignment

        # Select an unassigned variable
        var = self.select_unassigned_variable(assignment)

        # Iterate over the domain values of the variable
        for value in self.order_domain_values(var, assignment):
            assignment[var] = value

            if self.consistent(assignment):
                # Recursively try to complete assignment
                result = self.backtrack(assignment)
                if result is not None:
                    return result
            # 6. If we reach here, need to backtrack
            del assignment[var] 
    
        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
