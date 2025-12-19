import math
board = [" " for _ in range(9)]

def print_board():
    print("\n")
    for i in range(3):
        row = "| " + " | ".join(board[i*3:(i+1)*3]) + " |"
        print(row)
    print("\n")

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]
    for combo in win_conditions:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def empty_cells():
    return [i for i, spot in enumerate(board) if spot == " "]

def is_draw():
    return " " not in board


def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for cell in empty_cells():
            board[cell] = "O"
            score = minimax(False)
            board[cell] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for cell in empty_cells():
            board[cell] = "X"
            score = minimax(True)
            board[cell] = " "
            best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    best_move = None

    for cell in empty_cells():
        board[cell] = "O"
        score = minimax(False)
        board[cell] = " "
        if score > best_score:
            best_score = score
            best_move = cell

    board[best_move] = "O"


def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move in empty_cells():
                board[move] = "X"
                break
            else:
                print("Invalid move, try again!")
        except:
            print("Enter a number between 1 and 9!")
print("Welcome to Tic Tac Toe!")
print("You are X, AI is O.")

while True:
    print_board()

    
    player_move()
    if check_winner("X"):
        print_board()
        print("🎉 You win!")
        break

    if is_draw():
        print_board()
        print("It's a draw!")
        break

    
    ai_move()
    if check_winner("O"):
        print_board()
        print("😎 AI wins!")
        break

    if is_draw():
        print_board()
        print("It's a draw!")
        break
