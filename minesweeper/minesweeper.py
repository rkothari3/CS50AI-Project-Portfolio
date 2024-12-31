import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        # Creates a 2D Array -> In this case, a board
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        # While # of mines != max mines
        while len(self.mines) != mines:
            # Pick a random coordinate on board
            # (height), (width) bound
            i = random.randrange(height)
            j = random.randrange(width)
            # If mine not already there, then add the mine there and switch to True
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        # "Any time the number of cells is equal to the count, we know that all of that sentence’s cells must be mines."
        # If the number of cells is equal to the count and the count is greater than 0,
        # then all cells in this sentence must be mines.
        if len(self.cells) == self.count and self.count > 0:
            return self.cells  # Return the cells as known mines
        else:
            # Otherwise, return an empty set as no mines are known for sure
            return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        # "Any time we have a sentence whose count is 0, we know that all of that sentence’s cells must be safe."
        if self.count == 0:
            return self.cells
        else:
            return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        # When is a cell known to be a mine?
        # "if our AI knew the sentence {A, B, C} = 2, and we were told that C is a mine, we could remove C from the sentence and decrease the value of count (since C was a mine that contributed to that count), giving us the sentence {A, B} = 1. This is logical: if two out of A, B, and C are mines, and we know that C is a mine, then it must be the case that out of A and B, exactly one of them is a mine."
        if cell in self.cells:
            self.cells.remove(cell) # Remove cell from the set
            self.count -= 1 # Deduct the count

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.remove(cell) # Remove the cell, but don't deduct count


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # Step 1: Mark the cell as a move that has been made
        self.moves_made.add(cell)
        
        # This step records the cell as one that has been clicked or revealed by the player. 
        # It helps in tracking which cells have already been processed to avoid redundant operations.
        
        # Step 2: Mark the cell as safe
        self.mark_safe(cell)
        
        # This step updates the internal knowledge representation to indicate that the cell is safe.
        # It ensures that the AI does not consider this cell as a potential mine in future decisions.
        
        # Step 3: Add a new sentence to the AI's knowledge base based on the value of `cell` and `count`
        # Find all neighboring cells
        neighbors = set()
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                # Ignore the cell itself
                if (i, j) == cell:
                    continue
                # Ignore cells already known to be safe
                if (i, j) in self.safes:
                    continue
                # If the cell is a known mine, decrement the count of mines
                if (i, j) in self.mines:
                    count -= 1 
                    continue
                # Add the cell to neighbors if it is within bounds
                if 0 <= i < self.height and 0 <= j < self.width:
                    neighbors.add((i, j))
        
        # Create a new sentence with the neighboring cells and the count of mines
        new_sentence = Sentence(neighbors, count)
        # Add the new sentence to the knowledge base
        self.knowledge.append(new_sentence)
        
        # This step constructs a logical sentence representing the relationship between the neighboring cells and the count of mines.
        # It adds this sentence to the AI's knowledge base, which is used to infer the status of other cells.
        
        # Step 4: Mark any additional cells as safe or as mines if it can be concluded based on the AI's knowledge base
        # Create a copy of knowledge list to avoid modification during iteration
        knowledge_copy = self.knowledge.copy()
        
        for sentence in knowledge_copy:
            # Remove empty sentences from the knowledge base
            if len(sentence.cells) == 0:
                self.knowledge.remove(sentence)
                continue
                
            # Get copies of known mines and safes from the sentence
            known_mines = sentence.known_mines().copy()
            known_safes = sentence.known_safes().copy()
            
            # Mark all known mines
            for mine in known_mines:
                self.mark_mine(mine)
            # Mark all known safes
            for safe in known_safes:
                self.mark_safe(safe)
        
        # This step iterates through the knowledge base to identify cells that can be conclusively marked as safe or mines.
        # It updates the knowledge base accordingly, ensuring that the AI has the most accurate information.
        
        # Step 5: Add any new sentences to the AI's knowledge base if they can be inferred from existing knowledge
        # Create another copy for pair comparison
        knowledge_copy = self.knowledge.copy()
        
        for sentence1 in knowledge_copy:
            for sentence2 in knowledge_copy:
                # If sentence1 is a subset of sentence2, create a new inferred sentence
                if sentence1 != sentence2 and sentence1.cells.issubset(sentence2.cells):
                    # The new sentence's cells are the difference between sentence2 and sentence1
                    new_sentence_cells = sentence2.cells - sentence1.cells
                    # The new sentence's count is the difference between sentence2's count and sentence1's count
                    new_sentence_count = sentence2.count - sentence1.count
                    # Create the new sentence
                    new_sentence = Sentence(new_sentence_cells, new_sentence_count)
                    
                    # Add the new sentence to the knowledge base if it is not already present
                    if new_sentence not in self.knowledge:
                        self.knowledge.append(new_sentence)
        
        # This step performs logical inference by comparing pairs of sentences in the knowledge base.
        # If one sentence is a subset of another, it derives a new sentence representing the difference.
        # This helps in uncovering new information about the cells, further refining the AI's knowledge.

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        # Return a safe cell to choose on the Minesweeper board
        # if the safe move is not already made
        for safe in self.safes:
            if safe not in self.moves_made:
                return safe
        # Otherwise, return None
        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        # First check if there are any possible moves left
        possible_moves = []
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) not in self.moves_made and (i, j) not in self.mines:
                    possible_moves.append((i, j))
        
        if not possible_moves:
            return None
            
        return random.choice(possible_moves)
    

