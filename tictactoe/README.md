# Tic-Tac-Toe AI

The **Tic-Tac-Toe AI** project implements an intelligent agent capable of playing the classic game of Tic-Tac-Toe optimally using the **Minimax algorithm**. This AI ensures that it never loses and always makes the best possible moves, even against a human opponent. The project includes a graphical user interface (GUI) for an interactive gameplay experience.

## Features
- **Optimal AI Gameplay**: The AI uses the **Minimax algorithm** to evaluate all possible moves and choose the best one, ensuring it never loses.
- **Graphical Interface**: A user-friendly GUI powered by **Pygame** allows players to interact with the game visually.
- **Dynamic Game States**: Supports real-time computation of valid moves, game outcomes, and player turns.
- **Tie Guarantee**: Since Tic-Tac-Toe is a solved game, the AI ensures a tie if both players play optimally.

## Technologies Used
- **Python 3.12**
- **Minimax Algorithm** for decision-making
- **Alpha-Beta Pruning** to improve compute efficiency
- **Pygame** for graphical user interface
- Recursive functions for evaluating game states

## How It Works
1. The game starts with an empty board, and the player (X or O) alternates turns.
2. The AI evaluates all possible moves using the Minimax algorithm:
   - Maximizes its score when it's its turn.
   - Minimizes the opponent's score when it's their turn.
3. The program determines if the game is over after each move by checking for a winner or a tie.
4. Once implemented, users can play against the AI via the GUI by running `runner.py`.

## Learning Outcomes
This project demonstrates:
- The practical application of **game theory** and search algorithms in decision-making.
- How to implement recursive algorithms like Minimax to solve problems involving adversarial agents.
- The integration of AI logic with graphical interfaces for interactive applications.

## Example Usage
![image](https://github.com/user-attachments/assets/f218defd-8c30-4468-b8cf-fe074c61884c)

