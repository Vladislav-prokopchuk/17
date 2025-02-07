# tic_tac_toe_oop.py


class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        print("\n  0   1   2")
        for row_index, row in enumerate(self.board):
            print(f"{row_index} {' | '.join(row)}")
            if row_index < 2:
                print("  ---+---+---")
        print()

    def check_winner(self):
        # Перевірка рядків
        for row in self.board:
            if all(s == self.current_player for s in row):
                return True
        # Перевірка стовпців
        for col in range(3):
            if all(self.board[row][col] == self.current_player for row in range(3)):
                return True
        # Перевірка діагоналей
        if all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def make_move(self):
        while True:
            try:
                row, col = map(
                    int,
                    input(
                        f"Гравець {self.current_player}, введіть рядок і стовпчик (0-2) через пробіл: "
                    ).split(),
                )
                if self.board[row][col] == " ":
                    self.board[row][col] = self.current_player
                    break
                else:
                    print("Це поле вже зайняте!")
            except (ValueError, IndexError):
                print("Невірний ввід! Спробуйте ще раз.")

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play_game(self):
        while True:
            self.print_board()
            self.make_move()

            if self.check_winner():
                self.print_board()
                print(f"Гравець {self.current_player} виграв!")
                break

            if self.check_draw():
                self.print_board()
                print("Нічия!")
                break

            self.switch_player()


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
