"""
Tic Tac Toe Player
"""

import copy
X = "X"
O = "O"
EMPTY = None


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
    if(terminal(board)):
        return -1
    if board==initial_state():
        return X    
    count=0
    for i in board:
        for j in i:
            if j==EMPTY: count=count+1
    if count%2==0: 
        return O
    else : 
        return X        



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board): return -1
    ac=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==None:ac.add((i,j))
    return ac        

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    move=player(board)
    newb=copy.deepcopy(board)
    try:
        if newb[action[0]][action[1]]==EMPTY:
            newb[action[0]][action[1]]=move
    except:
        raise Exception("It's already filled!!")
    return newb
     
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0]==board[1][1]==board[2][2] : return board[0][0]
    if board[2][0]==board[1][1]==board[0][2] : return board[2][0]
    
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] : return board[i][0]
        if board[0][i]==board[1][i]==board[2][i] : return board[0][i]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board)): return True
    for i in board:
        for j in i:
            if j==None: return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board): 
        won=winner(board)
        if won==None: return 0
        elif won==X: return 1
        else       : return -1 


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    person=player(board)
    if person==X:
     if board==initial_state():
         return (1,1)
     v=-99999
     for action in actions(board):
         v=MIN_VALUE(result(board,action))
         if v==1: return action
         elif v==0: move=action  
    elif person==O:
        u=99999
        for action in actions(board):
            u=MAX_VALUE(result(board,action))
            if u==-1:
                return action
            elif u==0:
                move=action
    else:
        move=None
    return move                    

def MIN_VALUE(state):
    if terminal(state):
        return utility(state)
    u=99999
    for action in actions(state):
        u=min(u,MAX_VALUE(result(state,action)))
    return u


def MAX_VALUE(state):
    if terminal(state):
        return utility(state)
    v=-99999
    for action in actions(state):
        v=max(v,MIN_VALUE(result(state,action)))
    return v        
