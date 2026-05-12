import random
import re

class Minesweeper:
    def __init__(self, rows=9, cols=9, mines=10):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.reset_board()

    def reset_board(self):
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.mine_board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.revealed = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.flagged = [[False for _ in range(self.cols)] for _ in range(self.cols)]
        self.game_over = False
        self.first_move = True
        self.won = False

    def generate_mines(self, first_r=None, first_c=None):
        positions = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        if first_r is not None:
            positions.remove((first_r, first_c))

        mine_positions = random.sample(positions, self.mines)
        for r, c in mine_positions:
            self.mine_board[r][c] = 'M'

        for r in range(self.rows):
            for c in range(self.cols):
                if self.mine_board[r][c]!= 'M':
                    self.mine_board[r][c] = self.count_adjacent_mines(r, c)

    def count_adjacent_mines(self, r, c):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if self.mine_board[nr][nc] == 'M':
                        count += 1
        return count

    def print_board(self):
        print("\n " + " ".join(str(i) for i in range(self.cols)))
        print(" " + "--" * self.cols)
        for r in range(self.rows):
            row_str = f"{r} |"
            for c in range(self.cols):
                if self.game_over and self.mine_board[r][c] == 'M' and not self.flagged[r][c]:
                    row_str += "* " # Show all mines when game ends
                elif self.flagged[r][c]:
                    row_str += "F "
                elif not self.revealed[r][c]:
                    row_str += "■ "
                elif self.mine_board[r][c] == 'M':
                    row_str += "* "
                elif self.mine_board[r][c] == 0:
                    row_str += ". "
                else:
                    row_str += f"{self.mine_board[r][c]} "
            print(row_str)
        print(f"\nMines: {self.mines} | Flags: {sum(row.count(True) for row in self.flagged)}")

    def reveal(self, r, c):
        if not (0 <= r < self.rows and 0 <= c < self.cols):
            return False
        if self.flagged[r][c] or self.revealed[r][c]:
            return True

        if self.first_move:
            self.mine_board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
            self.generate_mines(r, c)
            self.first_move = False

        self.revealed[r][c] = True

        if self.mine_board[r][c] == 'M':
            self.game_over = True
            self.won = False
            return False

        if self.mine_board[r][c] == 0:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    self.reveal(r + dr, c + dc)
        return True

    def toggle_flag(self, r, c):
        if 0 <= r < self.rows and 0 <= c < self.cols and not self.revealed[r][c]:
            self.flagged[r][c] = not self.flagged[r][c]

    def check_win(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.mine_board[r][c]!= 'M' and not self.revealed[r][c]:
                    return False
        return True

    def play_round(self):
        self.reset_board()
        print("\n=== NEW GAME ===")
        print("Commands: r row col = reveal, f row col = flag, q = quit")
        print("Symbols: ■ = hidden, F = flag,. = empty, * = mine, 1-8 = numbers")

        while not self.game_over:
            self.print_board()

            if self.check_win():
                self.game_over = True
                self.won = True
                self.print_board()
                print("\n🎉 YOU WIN! All safe cells revealed!")
                break

            move = input("\nYour move: ").strip().lower()

            if move == 'q':
                self.game_over = True
                print("Game ended.")
                return 'quit'

            match = re.match(r'([rf])\s+(\d+)\s+(\d+)', move)
            if not match:
                print("Invalid input. Use: r row col or f row col")
                continue

            action, r, c = match.groups()
            r, c = int(r), int(c)

            if action == 'f':
                self.toggle_flag(r, c)
            elif action == 'r':
                if not self.reveal(r, c):
                    self.print_board()
                    print("\n💥 BOOM! You hit a mine. Game over!")

        return 'won' if self.won else 'lost'

def main():
    print("=== MINESWEEPER ===")
    # Change difficulty here: rows, cols, mines
    rows, cols, mines = 9, 9, 10 # Beginner
    # rows, cols, mines = 16, 16, 40 # Intermediate
    # rows, cols, mines = 16, 30, 99 # Expert

    game = Minesweeper(rows, cols, mines)

    while True:
        result = game.play_round()

        if result == 'quit':
            break

        while True:
            again = input("\nPlay again? y/n: ").strip().lower()
            if again in ['y', 'yes']:
                break
            elif again in ['n', 'no', 'q']:
                print("Thanks for playing!")
                return
            else:
                print("Please enter y or n")

if __name__ == "__main__":
    main()
