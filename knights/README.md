# Knights and Knaves

The **Knights and Knaves** project is a logic-based AI program inspired by Raymond Smullyan's famous puzzles. In these puzzles, characters are either knights, who always tell the truth, or knaves, who always lie. The objective is to determine the identity of each character based on their statements using **propositional logic** and **model-checking algorithms**.

This project encodes these puzzles into logical formulas, enabling an AI to deduce solutions by reasoning through the constraints of the puzzle.

## Features
- **Propositional Logic Representation**: Converts character statements into logical formulas to represent the problem.
- **Model Checking**: Uses a model-checking algorithm to evaluate all possible truth assignments and determine consistent solutions.
- **Multiple Puzzles**: Includes four unique puzzles of increasing complexity, each requiring logical reasoning to solve:
  - Puzzle 0: A single character claiming contradictory roles.
  - Puzzle 1: Two characters with one making a statement about both.
  - Puzzle 2: Two characters making contradictory claims about their identities.
  - Puzzle 3: Three characters with interdependent statements.

## Technologies Used
- **Python 3.12**
- Logical reasoning and propositional logic
- **Model-checking algorithm** for evaluating logical consistency

## How It Works
1. Each character's identity (knight or knave) is represented as a propositional symbol (e.g., `AKnight` for "A is a knight").
2. Statements made by characters are encoded as logical expressions that are true if and only if the speaker is a knight.
3. A knowledge base combines:
   - General rules about knights and knaves (e.g., a character cannot be both a knight and a knave).
   - Logical representations of each character's statements.
4. The AI uses the `model_check` function to evaluate all possible truth assignments and deduce which assignments satisfy all constraints.

## Key Files
- `logic.py`: Provides classes for propositional logic (e.g., `And`, `Or`, `Not`) and the `model_check` function.
- `puzzle.py`: Contains the knowledge bases for each puzzle and runs the model-checking algorithm.

## Learning Outcomes
This project demonstrates:
- How to encode real-world problems into **propositional logic**.
- The use of **model-checking algorithms** to solve logical puzzles.
- The power of AI in automating complex reasoning tasks.

