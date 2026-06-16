import random

# Game State
board_state = [[' ' for _ in range(3)] for _ in range(3)]
available_spots = ['00', '01', '02', '10', '11', '12', '20', '21', '22']

def show_spots():
    print("\nSpot Coordinates:")
    print("00 | 01 | 02", "10 | 11 | 12", "20 | 21 | 22", sep='\n')
    print("-" * 12)

def print_board():
    print()
    for row in board_state:
        print(" " + " | ".join(row))
    print()

def is_winner(board, player):
    """Pure function to determine if the given player has won."""
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)): return True
        if all(board[j][i] == player for j in range(3)): return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player: return True
    if board[0][2] == board[1][1] == board[2][0] == player: return True
    return False

def get_ai_move():
    """Evaluates options using look-ahead without mutating global state."""
    win_spots = []
    block_spots = []

    for move in available_spots:
        r, c = int(move[0]), int(move[1])
        
        # 1. Can AI ('O') win right here?
        board_state[r][c] = 'O'
        if is_winner(board_state, 'O'):
            win_spots.append(move)
        board_state[r][c] = ' ' # Undo

        # 2. Does AI need to block Player ('X')?
        board_state[r][c] = 'X'
        if is_winner(board_state, 'X'):
            block_spots.append(move)
        board_state[r][c] = ' ' # Undo

    if win_spots:   return random.choice(win_spots)
    if block_spots: return random.choice(block_spots)
    return random.choice(available_spots)

def play_game():
    show_spots()
    print("X goes first. Enter 'show' to view layout coordinates anytime.")
    
    while True:
        # --- PLAYER TURN ---
        move = input("Your move (X) - Choose spot: ").strip()
        
        if move == 'show':
            show_spots()
            continue
            
        if move not in available_spots:
            print("Invalid or occupied spot! Try again.")
            continue

        # Execute move
        available_spots.remove(move)
        board_state[int(move[0])][int(move[1])] = 'X'
        print_board()

        if is_winner(board_state, 'X'):
            print("Game Over. X wins!")
            break
            
        if not available_spots:
            print("It's a draw!")
            break

        # --- AI TURN ---
        print("My move (O):")
        ai_move = get_ai_move()
        available_spots.remove(ai_move)
        board_state[int(ai_move[0])][int(ai_move[1])] = 'O'
        print_board()

        if is_winner(board_state, 'O'):
            print("Game Over. O wins!")
            break
            
        if not available_spots:
            print("It's a draw!")
            break

if __name__ == '__main__':
    play_game()
