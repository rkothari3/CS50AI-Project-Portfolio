"""
Tic Tac Toe Player - Alpha-Beta Prunning for Minimax Algorithm - Make it more efficient!
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state(): # each list a row of the board. 3x3. EMPTY is None; therefore, Empty board
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    - Takes a board state as input.
    - Returns which player’s turn it is (either X or O).
    - In the initial game state, X gets the first move.
    - Subsequently, the player alternates with each additional move.
    - Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).
    """
    if board == initial_state():
        return X # If board is empty, X gets the first move.
    else:
        # Set both counts to 0
        count_X = 0
        count_O = 0
        # .count() method returns the number of occurrences of a substring in the given string.
        for row in board:
            count_X += row.count(X) # add the number of time X is in the row.
            count_O += row.count(O) # add the number of time O is in the row.
        if count_X > count_O: # If X has more moves than O, it is O's turn.
            return O
        else:
            return X # Otherwise, it is X's turn.


def actions(board):
    """
    - The actions function should return a set of all of the possible actions that can be taken on a given board.
    - Each action should be represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
    - Possible moves are any cells on the board that do not already have an X or an O in them.
    - Any return value is acceptable if a terminal board is provided as input.
    """
    possible_moves = set() # set is a data structure that stores unique elements.
    for i in range(3): 
        for j in range(3):
            if board[i][j] == EMPTY: # If the cell is empty, add it to the set.
                possible_moves.add((i, j))
    return possible_moves


def result(board, action):
    """
    - The result function takes a board and an action as input, and should return a new board state, without modifying the original board.
    - If action is not a valid action for the board, your program should raise an exception.
    - The returned board state should be the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action.
    - Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation. This means that simply updating a cell in board itself is not a correct implementation of the result function. You’ll likely want to make a deep copy of the board first before making any changes.
    """
    # Make a deep copy of the board.
    new_board = copy.deepcopy(board)

    if action not in actions(board):
        print(f"Invalid action: {action}")
        print(f"Possible actions: {actions(board)}")
        raise Exception("Invalid action")
    else:
        i, j = action
        new_board[i][j] = player(board) # If player(X) is making a move, set the cell (i, j) to X.

    return new_board

def winner(board):
    """
    - The winner function should accept a board as input, and return the winner of the board if there is one.
    - If the X player has won the game, your function should return X. If the O player has won the game, your function should return O.
    - One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
    - If there is no winner, the function should return None.
    """
    # Check for horizontal win
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O
    
    # Check for vertical win
    for i in range(3):  # i corresponds to the column index
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]  # Return the player who won
    
    # Check for diagonal win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]  # Return the player who won
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]  # Return the player who won
    
    # If no winner, return None
    return None


def terminal(board):
    '''
    - The terminal function should accept a board as input, and return a boolean value indicating whether the game is over.
    - If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return True.
    - Otherwise, the function should return False if the game is still in progress.
    '''
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True

def utility(board):
    """
    - The utility function should accept a terminal board as input and output the utility of the board.
    - If X has won the game, the utility is 1.
    - If O has won the game, the utility is -1.
    - If the game has ended in a tie, the utility is 0.
    - You may assume utility will only be called on a board if terminal(board) is True.
    """
    if winner(board) == X: # If X has won the game, the utility is 1.
        return 1
    elif winner(board) == O: # If O has won the game, the utility is -1.
        return -1
    else:
        return 0
    # note: utility only called on a board if terminal(board) is True.


def minimax(board):
    """
    - The minimax function should take a board as input, and return the optimal move for the player to move on that board.
    - The move returned should be the optimal action (i, j) that is one of the allowable actions on the board.
    - If multiple moves are equally optimal, any of those moves is acceptable.
    - If the board is a terminal board, the minimax function should return None.
    """
    if terminal(board):
        return None
    
    # Alpha-Beta Prunning
    # - Alpha: best value that the maximizing player (e.g., X) currently can guarantee at that level or above.
    # - Beta: best value that the minimizing player (e.g., O) currently can guarantee at that level or above.

    def max_value(board, alpha, beta): 
        # max player tries to maximize the minimum utility value (score)
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action), alpha, beta))
            if v >= beta: # if v (max value) is greater than or equal to beta, return v.
                return v
            alpha = max(alpha, v) # update alpha to the maximum of alpha and v.
        return v
    
    def min_value(board, alpha, beta): 
        # min player tries to minimize the maximum utility value (score)
        if terminal(board):
            return utility(board)
        v = math.inf
        for action in actions(board):
            v = min(v, max_value(result(board, action), alpha, beta))
            if v <= alpha: # if v (min value) is less than or equal to alpha, return v.
                return v
            beta = min(beta, v) # update beta to the minimum of beta and v.
        return v

    # Determine the current player
    current_player = player(board)
    
    if current_player == X:
        # If the current player is X, try to maximize the score
        best_value = -math.inf
        best_action = None
        alpha = -math.inf
        beta = math.inf
        for action in actions(board):
            action_value = min_value(result(board, action), alpha, beta)
            if action_value > best_value:
                best_value = action_value
                best_action = action
            alpha = max(alpha, best_value)
    else:
        # If the current player is O, try to minimize the score
        best_value = math.inf
        best_action = None
        alpha = -math.inf
        beta = math.inf
        for action in actions(board):
            action_value = max_value(result(board, action), alpha, beta)
            if action_value < best_value:
                best_value = action_value
                best_action = action
            beta = min(beta, best_value)

    # Return the best action found
    return best_action
