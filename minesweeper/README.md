# Minesweeper AI

The **Minesweeper AI** project implements an intelligent agent that can play the classic Minesweeper game. By leveraging **propositional logic** and **knowledge-based reasoning**, the AI deduces the locations of hidden mines and identifies safe cells to click. The AI uses logical inference to make moves, ensuring accuracy and efficiency in solving the game.

## Features
- **Knowledge Representation**: Represents game knowledge as logical sentences, associating cells with mine probabilities.
- **Logical Inference**: Infers safe cells and mine locations using rules such as:
  - If the count of neighboring mines equals 0, all neighbors are safe.
  - If the count equals the number of unknown neighbors, all neighbors are mines.
- **Subset Reasoning**: Derives new knowledge by comparing subsets of known sentences.
- **Safe and Random Moves**: Prioritizes safe moves but can make random moves when necessary.

## Technologies Used
- **Python 3.12**
- Propositional logic for knowledge representation
- Object-oriented programming for game mechanics
- **Pygame** for graphical interface

## How It Works
1. The game board is represented as a grid where each cell is either a mine or safe.
2. The AI maintains a knowledge base of logical sentences about the board:
   - Each sentence consists of a set of cells and a count of how many contain mines.
3. When a safe cell is clicked, the AI:
   - Updates its knowledge base with information about neighboring cells.
   - Infers new safe cells or mines based on logical rules.
4. The AI makes moves based on its knowledge:
   - If a safe move is known, it clicks that cell.
   - If no safe move exists, it selects a random unexplored cell.

### Logical Inference Example:
If the AI knows `{A, B, C} = 2` (two of these cells are mines) and `{A, B} = 1` (one of these two is a mine), it can infer that `{C} = 1` (C is a mine).

## Key Classes in `minesweeper.py`
### `Sentence`
- Represents logical sentences about the board.
- Functions:
  - `known_mines`: Returns cells that are definitively mines.
  - `known_safes`: Returns cells that are definitively safe.
  - `mark_mine` / `mark_safe`: Updates the sentence when a cell is identified as a mine or safe.

### `MinesweeperAI`
- Implements the AI logic for playing Minesweeper.
- Functions:
  - `add_knowledge`: Updates the knowledge base with new information and infers new facts.
  - `make_safe_move`: Returns a known safe move if available.
  - `make_random_move`: Selects a random unexplored cell if no safe moves exist.

## Learning Outcomes
This project demonstrates:
- How to use **propositional logic** for reasoning under uncertainty.
- The application of **knowledge-based agents** in solving real-world problems.
- Efficient problem-solving using logical inference and subset reasoning.

## Example Usage
![image](https://github.com/user-attachments/assets/54ba1a66-a6b5-4bc7-8845-676a99a47291)


