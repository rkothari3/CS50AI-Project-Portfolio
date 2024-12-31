# Nim AI

The **Nim AI** project implements an intelligent agent that teaches itself to play the game of Nim using **Reinforcement Learning**. By playing thousands of games against itself, the AI learns the optimal strategy for removing objects from piles to ensure victory. The project leverages **Q-learning**, a model-free reinforcement learning algorithm, to associate rewards with specific actions in given game states.

## Features
- **Q-Learning Algorithm**:
  - Learns the optimal strategy by updating Q-values for state-action pairs based on rewards.
  - Rewards:
    - \(+1\) for actions leading to a win.
    - \(-1\) for actions leading to a loss.
    - \(0\) for intermediate actions.
- **Epsilon-Greedy Action Selection**:
  - Balances exploration (choosing random actions) and exploitation (choosing the best-known action).
- **Self-Play Training**:
  - Trains by simulating thousands of games against itself to refine its strategy.
- **Human vs AI Gameplay**:
  - Allows a human player to compete against the trained AI.

## Technologies Used
- **Python 3.12**
- Reinforcement learning with Q-learning
- Object-oriented programming for game mechanics

## How It Works
1. **Game Representation**:
   - The game state is represented as a list of integers, where each integer corresponds to the number of objects in a pile.
   - Actions are represented as tuples \((i, j)\), where \(i\) is the pile index and \(j\) is the number of objects to remove from that pile.
2. **Training**:
   - The AI plays thousands of games against itself.
   - During each game, it updates its Q-values using the formula:
![image](https://github.com/user-attachments/assets/2ff78918-2231-4c85-a283-8f971ae959e4)
3. **Gameplay**:
   - During gameplay, the AI selects actions using an epsilon-greedy strategy:
     - With probability (epsilon), it chooses a random action (exploration).
     - With probability (1 - epsilon), it chooses the action with the highest Q-value (exploitation).

## Key Functions in `nim.py`
### `get_q_value(state, action)`
- Returns the Q-value for a given state-action pair. If no value exists, returns \(0\).

### `update_q_value(state, action, old_q, reward, future_rewards)`
- Updates the Q-value using the Q-learning formula.

### `best_future_reward(state)`
- Returns the maximum future reward for any available action in a given state.

### `choose_action(state, epsilon)`
- Selects an action using epsilon-greedy strategy.

## Learning Outcomes
This project demonstrates:
- How reinforcement learning can be used to train an AI agent without explicit programming of strategies.
- The implementation and application of **Q-learning** in decision-making tasks.
- Balancing exploration and exploitation with an epsilon-greedy approach.

## Example Usage
```bash
$ python play.py
Playing training game 1
Playing training game 2
Playing training game 3
...
Playing training game 9999
Playing training game 10000
Done training

Piles:
Pile 0: 1
Pile 1: 3
Pile 2: 5
Pile 3: 7

AI's Turn
AI chose to take 1 from pile 2.
