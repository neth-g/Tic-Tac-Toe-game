import random, copy

# global variables
board = [[' ' for i in range(3)] for j in range(3)]
spot_names = [[str(i)+str(j) for j in range(3)] for i in range(3)]
available_spots = []
for i in range(3):
    for j in range(3): available_spots.append(str(i)+str(j))

# display the board spot names
def Help():
    print()
    for i in spot_names:
        print(*i, sep=' | ')
    print()

# display the board
def showBoard():
    print()
    for i in board:
        print(*i, sep = ' | ')
    print()

# make move function
def makeMove(token, location, board, available_spots):
    i,j=int(location[0]),int(location[1])
    board[i][j]=token
    available_spots.remove(location)

# player turn
def playerTurn():
    location = input("Where do you want to place your token? ")
    if location not in available_spots:
        if location=='?': Help()
        else: print("Invalid value entered. Please try again.")
        playerTurn()
    else:
        makeMove('X', location, board, available_spots)

# computer turn
def computerTurn(token1, token2, board, available_spots):
    location=random.choice(bestOptions(board, available_spots))
    makeMove(token1, location, board, available_spots)

def bestOptions(board, available_spots):
    scores = {}
    for i in available_spots:
        temp_board = copy.deepcopy(board)
        temp_available_spots = copy.deepcopy(available_spots)
        makeMove('O', i, temp_board, temp_available_spots)
        score = simulatePath('X','O',temp_board,temp_available_spots)
        scores |= {i:score}
    print(scores)
    best_choices = [k for k,v in scores.items() if v==max(scores.values())]
    return best_choices


def simulatePath(token1, token2, board, available_spots):
    score = 0
    if checkWin('O', board): score+=1
    elif checkWin('X', board): score-=1
    elif available_spots==[]: score+=0
    else:
        for i in available_spots:
            temp_board = copy.deepcopy(board)
            temp_available_spots = copy.deepcopy(available_spots)
            makeMove(token1, i, temp_board, temp_available_spots)
            score += simulatePath(token2, token1, temp_board, temp_available_spots)
    return score


# win checking logic
def checkWin(token, board):
    for i in range(3):
        if all(board[i][j]==token for j in range(3)): return True
        if all(board[j][i]==token for j in range(3)): return True
    if all(board[i][i]==token for i in range(3)): return True
    if all(board[i][2-i]==token for i in range(3)): return True
    return False

# order of turns and wincheck logic - master program
def turnOrder():
    while True:
        print("It is your turn!")
        playerTurn()
        showBoard()
        if checkWin('X', board):
            print("You win! Congratulations!")
            print("Game over.")
            break
        if available_spots==[]:
            print("It's a tie! Good game.")
            print("Game over.")
            break
        print("It is now my turn.")
        computerTurn('O', 'X', board, available_spots)
        showBoard()
        if checkWin('O', board):
            print("I win! Better luck next time.")
            print("Game over.")
            break

# all the code is here
def main():
    print("Welcome to the tic-tac-toe game!")
    print("These are the names of each location.")
    Help()
    print("In order to see this again, enter '?'")
    turnOrder()



main
