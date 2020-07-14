"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
optimalActionX=None
optimalActionO=None

def draw(board):
    """
    Returns boolean value indicating if the game is a draw. No one won. All cells have been filled.
    """
    sum_none=0
    for row in board:
        sum_none+=row.count(None)

    if sum_none==0:
        return True

    return False


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    sum_x=0
    sum_o=0

    for row in board:
        sum_x+=row.count('X')
        sum_o+=row.count('O')

    if terminal(board):
        return X

    elif(sum_x==sum_o):
        return X

    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    if terminal(board):
        return {(0,0)}

    free_moves=set()

    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                free_moves.add((i,j))

    return free_moves


def result(board, action):                                                          #action is tuple (i,j)
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # print('Action in result',action)
    (i,j)=action

    if board[i][j] is not EMPTY:
        raise Exception('InvalidAction')

    board_copy = copy.deepcopy(board)                                               #Making copy

    if player(board_copy)==X:                                                       #Whose turn
        board_copy[i][j]=X
        return board_copy

    board_copy[i][j]=O
    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0]==X and board[1][0]==X and board[2][0]==X:                        #Vertical X wins
        return X    
    if board[0][1]==X and board[1][1]==X and board[2][1]==X:                        #Vertical X wins
        return X
    if board[0][2]==X and board[1][2]==X and board[2][2]==X:                        #Vertical X wins
        return X
    if board[0][0]==X and board[0][1]==X and board[0][2]==X:                        #Horizontal X wins
        return X
    if board[1][0]==X and board[1][1]==X and board[1][2]==X:                        #Horizontal X wins
        return X
    if board[2][0]==X and board[2][1]==X and board[2][2]==X:                        #Horizontal X wins
        return X
    if board[0][0]==X and board[1][1]==X and board[2][2]==X:                        #Diagonally X wins
        return X
    if board[0][2]==X and board[1][1]==X and board[2][0]==X:                        #Diagonally X wins
        return X

        
    if board[0][0]==O and board[1][0]==O and board[2][0]==O:                        #Vertical O wins
        return O
    if board[0][1]==O and board[1][1]==O and board[2][1]==O:                        #Vertical O wins
        return O
    if board[0][2]==O and board[1][2]==O and board[2][2]==O:                        #Vertical O wins
        return O
    if board[0][0]==O and board[0][1]==O and board[0][2]==O:                        #Horizontal O wins
        return O
    if board[1][0]==O and board[1][1]==O and board[1][2]==O:                        #Horizontal O wins
        return O
    if board[2][0]==O and board[2][1]==O and board[2][2]==O:                        #Horizontal O wins
        return O
    if board[0][0]==O and board[1][1]==O and board[2][2]==O:                        #Diagonally O wins
        return O
    if board[0][2]==O and board[1][1]==O and board[2][0]==O:                        #Diagonally O wins
        return O

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:                                                   #Either someone won, or the game is a draw. So don't play any more.
        return True

    elif draw(board) is True:                                                       #No one won. All boards filled.
        return True

    return False

def utility(board):                                                                 #This is called only if function terminal(board) returns True  
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1

    elif winner(board)==O:
        return -1

    elif (draw(board)):
        return 0

def maxValue(state, alpha, beta):
    
    if terminal(state):
        return utility(state)
    
    v=-math.inf

    # print('Possible actions maxvalue:', actions(state))
    for action in actions(state):
        # print(action)
        v=max( v, minValue(result(state,action),alpha, beta ) )
        
        if v>=beta:
            return v

        alpha = max(alpha, v)

    return v

def minValue(state, alpha, beta):
    
    if terminal(state):
        return utility(state)
    
    v=math.inf

    # print('Possible actions minvalue:', actions(state))
    for action in actions(state):
        # print('..',action)
        v=min( v, maxValue(result(state,action), alpha, beta) )

        if v <= alpha:
            return v
        beta = min(beta, v)

    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    turn=player(board)

    alpha=-1
    beta=1

    if turn==X:
        mx = -math.inf
        for action in actions(board):
            value = minValue(result(board, action), alpha, beta)
            if value > mx:
                mx = value
                optimal = action

    else:
        mn = math.inf
        for action in actions(board):
            value = maxValue(result(board, action), alpha, beta)
            if value < mn:
                mn = value
                optimal = action

    return optimal
