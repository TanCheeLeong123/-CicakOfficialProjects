import os

# Queen Toadstool & The Warp Pipes Reversi
# ⚫ = Black, ⚪ = White

EMPTY = "."
BLACK = "⚫"
WHITE = "⚪"
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def create_board():
    board = [[EMPTY for _ in range(8)] for _ in range(8)]
    board[3][3] = WHITE
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[4][4] = WHITE
    return board

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Queen Toadstool & The Warp Pipes Reversi 🍄")
    print("Black ⚫ vs White ⚪")
    print()
    print(" 0 1 2 3 4 5 6 7")
    for i, row in enumerate(board):
        print(i, " ".join(row))
    print()

def is_on_board(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def is_valid_move(board, x, y, player):
    if board[x][y]!= EMPTY:
        return False

    opponent = WHITE if player == BLACK else BLACK
    valid = False

    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        found_opponent = False

        while is_on_board(nx, ny) and board[nx][ny] == opponent:
            nx += dx
            ny += dy
            found_opponent = True

        if found_opponent and is_on_board(nx, ny) and board[nx][ny] == player:
            valid = True
            break

    return valid

def get_valid_moves(board, player):
    moves = []
    for x in range(8):
        for y in range(8):
            if is_valid_move(board, x, y, player):
                moves.append((x, y))
    return moves

def make_move(board, x, y, player):
    board[x][y] = player
    opponent = WHITE if player == BLACK else BLACK

    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        to_flip = []

        while is_on_board(nx, ny) and board[nx][ny] == opponent:
            to_flip.append((nx, ny))
            nx += dx
            ny += dy

        if is_on_board(nx, ny) and board[nx][ny] == player:
            for fx, fy in to_flip:
                board[fx][fy] = player

def get_score(board):
    black_score = sum(row.count(BLACK) for row in board)
    white_score = sum(row.count(WHITE) for row in board)
    return black_score, white_score

def game_over(board):
    return not get_valid_moves(board, BLACK) and not get_valid_moves(board, WHITE)

def play_reversi():
    board = create_board()
    current_player = BLACK # Mario goes first
    
    while not game_over(board):
        print_board(board)
        black_score, white_score = get_score(board)
        print(f"Score: Black {BLACK} {black_score} | White {WHITE} {white_score}")
        
        valid_moves = get_valid_moves(board, current_player)
        player_name = "Black" if current_player == BLACK else "White"
        
        if not valid_moves:
            print(f"{player_name} has no valid warp pipes! Skipping turn.")
            input("Press Enter to continue...")
            current_player = WHITE if current_player == BLACK else BLACK
            continue

        print(f"{player_name}'s turn {current_player}")
        print("Valid pipes:", " ".join([f"{x}{y}" for x, y in valid_moves]))
        
        try:
            move = input("Enter row,col to place your tile e.g. 2,3: ").strip()
            x, y = map(int, move.split(","))
            
            if (x, y) in valid_moves:
                make_move(board, x, y, current_player)
                current_player = WHITE if current_player == BLACK else BLACK
            else:
                print("Invalid warp pipe! You can't go there.")
                input("Press Enter to try again...")
        except:
            print("Bad input! Use format: row,col like 2,3")
            input("Press Enter to try again...")

    # Game over
    print_board(board)
    black_score, white_score = get_score(board)
    print("Game Over! No more warp pipes!")
    print(f"Final Score: Black {BLACK} {black_score} | White {WHITE} {white_score}")
    
    if black_score > white_score:
        print("Black wins!")
    elif white_score > black_score:
        print("White wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_reversi()
