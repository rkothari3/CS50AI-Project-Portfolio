# Crossword AI

The **Crossword AI** project is an intelligent system designed to generate complete crossword puzzles by solving them as a **Constraint Satisfaction Problem (CSP)**. By leveraging constraints like word lengths, overlaps, and uniqueness, the AI ensures that all words fit together in the puzzle's structure while adhering to logical rules.

## Features
- **Constraint Satisfaction Problem (CSP) Solver**:
  - Enforces **unary constraints**: Ensures words match the required length for each variable.
  - Enforces **binary constraints**: Ensures overlapping variables share consistent characters.
  - Enforces word uniqueness: No word is repeated in the puzzle.
- **AC-3 Algorithm**: Implements Arc Consistency to reduce the search space by pruning inconsistent values from variable domains.
- **Backtracking Search**:
  - Uses heuristics like **Minimum Remaining Values (MRV)** and **Degree Heuristic** to optimize variable selection.
  - Applies the **Least Constraining Value (LCV)** heuristic to prioritize domain values that leave the most options for neighboring variables.
- **Customizable Input**:
  - Accepts a puzzle structure file defining the grid layout.
  - Accepts a vocabulary file containing words to populate the crossword.

## Technologies Used
- **Python 3.12**
- Constraint satisfaction algorithms (AC-3, Backtracking)
- Heuristic-based optimization for CSP solving
- File parsing for crossword structures and word lists

## How It Works
1. The AI models the crossword as a CSP:
   - Variables represent sequences of blank cells (across or down).
   - Domains represent possible words that can fill those blanks.
   - Constraints enforce word length, shared character consistency, and uniqueness.
2. The solving process involves:
   - Enforcing **node consistency** by removing words that don't satisfy unary constraints (length).
   - Applying the AC-3 algorithm to enforce arc consistency by ensuring neighboring variables agree on overlapping letters.
   - Using backtracking search with heuristics to assign words to variables while satisfying all constraints.
3. The final solution is output as a completed crossword puzzle.

## Key Functions in `generate.py`
### `enforce_node_consistency`
- Ensures each variable's domain only contains words of the correct length.

### `revise`
- Makes one variable arc-consistent with another by removing conflicting values.

### `ac3`
- Enforces arc consistency across all variables using the AC-3 algorithm.

### `assignment_complete`
- Checks if all variables are assigned a value in a given assignment.

### `consistent`
- Verifies that an assignment satisfies all constraints (length, overlap, uniqueness).

### `order_domain_values`
- Orders domain values for a variable using the Least Constraining Value heuristic.

### `select_unassigned_variable`
- Selects an unassigned variable using MRV and Degree Heuristics.

### `backtrack`
- Performs backtracking search to find a complete assignment of words to variables.

## Learning Outcomes
This project demonstrates:
- How to model real-world problems as **Constraint Satisfaction Problems (CSP)**.
- The use of algorithms like **AC-3** and **Backtracking Search** for solving CSPs efficiently.
- The application of heuristics (**MRV**, **Degree**, and **LCV**) to optimize search processes.
- Practical implementation of AI techniques in generating structured puzzles.

## Example Usage
![image](https://github.com/user-attachments/assets/e77442b9-c0b5-4ab8-82e8-92074fcbb41b)
```bash
$ python generate.py data/structure1.txt data/words1.txt output.png
██████████████
███████M████R█
█INTELLIGENCE█
█N█████N████S█
█F██LOGIC███O█
█E█████M████L█
█R███SEARCH█V█
███████X████E█
██████████████

