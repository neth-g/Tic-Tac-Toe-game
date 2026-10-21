import random
import copy 

def play_game():
    #Setup
    board_state = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] #matrix for 9 spaces of the board
    available_spots=['00','01','02','10','11','12','20','21','22'] #keeping track of the spaces that are not yet occupied.
    #Instructions for the beginning
    print("Welcome to tic tac toe.")
    print("These are the board coordinates. We'll be using these to identify where we move.")
    show_spots()
    show_board(board_state)
    print("X goes first. You're playing X.")
    #Turn loop
    while True:    
        # PLAYER TURN
        result = player_turn(board_state, available_spots)
        if result == 'X': 
            print("You win! Game over!")
            break
        elif not available_spots: 
            print("It's a draw. Game over.")
            break
        elif result == 'try again':
            continue
        # COMPUTER TURN
        result = ai_turn(board_state, available_spots)
        if result == 'O':
            print("I win! Game over.")
            break
        # Computer does not have a check for draw because computer's turn will never cause a draw if player starts.


#Clarify which spot is given which name
def show_spots():
    print("00|01|02","10|11|12","20|21|22", sep='\n')

#Show the board after every move
def show_board(board):
    for i in board:
        print(i[0], i[1], i[2], sep = ' | ')

#Check whether the latest move has won the game or not.
def is_won(board, token):
    for i in range(3):
        if all(board[i][j] == token for j in range(3)): return True #rows
        if all(board[j][i] == token for j in range(3)): return True #columns
    if all(board[j][j] == token for j in range(3)): return True #left top to right bottom
    if board[2][0] == board[1][1] == board[0][2] == token: return True #right top to left bottom
    else: return False

def evaluate_board(board, available_spots):
    if is_won(board, 'O'): return +1
    if is_won(board, 'X'): return -1
    if not available_spots: return 0
    else: return None

def check_possibilities(board, available_spots, player):
    score = evaluate_board(board, available_spots)
    if score is not None: return score
    # computer's turn
    if player: 
        best_score = -20 #whatever is checked against it will be higher.
        for spot in list(available_spots): 
            # check this particular move
            i, j = int(spot[0]), int(spot[1])
            board[i][j]='O'
            available_spots.remove(spot)
            score = check_possibilities(board, available_spots, False)
            # reset board
            board[i][j]=' '
            available_spots.append(spot)
            # if this game goes relatively better to the previous one, put this one there.
            if best_score < score:
                best_score = score
        return best_score
    # player's turn
    else:
        best_score = 20
        for spot in list(available_spots): 
            # check this particular move
            i, j = int(spot[0]), int(spot[1])
            board[i][j]='X'
            available_spots.remove(spot)
            score = check_possibilities(board, available_spots, True)
            # reset board
            board[i][j]=' '
            available_spots.append(spot)
            # if this game goes relatively better to the previous one, put this one there.
            if best_score > score:
                best_score = score
        return best_score


def ai_move(board, available_spots):
    possibilities = {} #Dictionary that keeps spot:winning chances pairs for every remaining spot
    for spot in list(available_spots):
        virtual_board = copy.deepcopy(board)
        temp_available_spots = copy.deepcopy(available_spots)
        i,j = int(spot[0]), int(spot[1])
        virtual_board[i][j] = 'O'
        temp_available_spots.remove(spot)
        possibilities[spot] = check_possibilities(virtual_board, temp_available_spots, False)
    best_spots = [k for k, v in possibilities.items() if v == max(possibilities.values())]
    return random.choice(best_spots)


#player's turn
def player_turn(board, available_spots):
    while True:
        print("Your move.")
        move = input("Where do you want to place your token? 'X': ")
        if move == 'show':
            show_spots()
        elif move not in available_spots:
            print("Unrecognised response. Please try again.")
        else:
            i,j = int(move[0]), int(move[1])
            board[i][j] = 'X'
            show_board(board)
            available_spots.remove(move)
            if is_won(board, 'X'): return 'X'
            else: return "continue"

#computer's turn
def ai_turn(board, available_spots):
    print("My turn.")
    move = ai_move(board, available_spots)
    i,j = int(move[0]), int(move[1])
    board[i][j] = 'O'
    show_board(board)
    available_spots.remove(move)
    if is_won(board, 'O'): return 'O'
    else: return "continue"
    

play_game()

