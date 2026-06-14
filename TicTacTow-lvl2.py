import random

s = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] #matrix for 9 spaces of the board
availableSpots=['00','01','02','10','11','12','20','21','22'] #keeping track of the spaces that are not yet occupied.
win=0 #variable to keep track of whether or not the game has been won.
blockSpots=[]
winSpots=[]
move=' '

#Clarify which spot is given which name
def showSpots():
    print("00|01|02","10|11|12","20|21|22", sep='\n')

#Show the board after every move
def board():
    for i in s:
        print(i[0], i[1], i[2], sep=' | ')

#Check whether the latest move has won the game or not.
def winCheck(move):
    global win
    i = int(move[0])
    j = int(move[1])
    # check column corresponding to the move
    if s[0][j]==s[1][j]==s[2][j]:
        win+=1
    elif s[i][0]==s[i][1]==s[i][2]:
        win+=1
    elif move=='00' or move=='11' or move=='22':
        if s[0][0]==s[1][1]==s[2][2]:
            win+=1
    elif move=='02' or move=='11' or move=='20':
        if s[0][2]==s[1][1]==s[2][0]:
            win+=1

    
showSpots()

def nearWin(availableSpots):
    global blockSpots
    global winSpots
    global win
    winSpots=[]
    blockSpots=[]
    for mov in availableSpots:
        i = int(mov[0])
        j = int(mov[1])
        s[i][j]='O'
        winCheck(mov)
        if win>=1:
            winSpots.append(mov)
            win=0
        else:
            pass
        s[i][j]=' '
    for mov in availableSpots:
        i = int(mov[0])
        j = int(mov[1])
        s[i][j]='X'
        winCheck(mov)
        if win>=1:
            blockSpots.append(mov)
            win=0
        else:
            pass
        s[i][j]=' '
    

#During a turn
def turn():
    global move
    while win==0:
        #player turn
        move = input("Your move. Where do you want to place your token?")
        if move == 'show':
            showSpots()
            continue
        else:
            try:
                s[int(move[0])][int(move[1])]='X'
                availableSpots.remove(move)
                board()
                winCheck(move)
            except ValueError:
                print("Ivaild option entered. Please try again.")
                continue
        #computer turn
        if win==1:
            break
        elif availableSpots==[]:
            print("It's a draw!")
            break
        else:
            print("My move.")
            nearWin(availableSpots)
            if winSpots!=[]:
                move=random.choice(winSpots)
            elif blockSpots != []:
                move=random.choice(blockSpots)
            else:
                move=random.choice(availableSpots)
            availableSpots.remove(move)
            s[int(move[0])][int(move[1])]='O'
            board()
            winCheck(move)
                

#Beginning instructions
print("enter 'show' to view the names of the spaces again.")
print("X goes first.")

#main
    
turn()
if win>0:
    print("Game over.")
    print(s[int(move[0])][int(move[1])], "wins. ")
