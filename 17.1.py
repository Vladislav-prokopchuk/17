# Функція для виведення поля гри з покращеним форматом
def print_board(board):
    print("\n" + "  0   1   2")
    for row_index, row in enumerate(board):
        print(f"{row_index} {' | '.join(row)}")
        if row_index < 2:
            print("  ---+---+---")
    print()


# Функція для перевірки перемоги
def check_winner(board, player):
    # Перевірка рядків
    for row in board:
        if all(s == player for s in row):
            return True
    # Перевірка стовпців
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Перевірка діагоналей
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


# Функція для перевірки нічиєї
def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True


# Функція для виконання ходу
def make_move(board, player):
    while True:
        try:
            row, col = map(
                int,
                input(
                    f"Гравець {player}, введіть рядок і стовпчик (0-2) через пробіл: "
                ).split(),
            )
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Це поле вже зайняте!")
        except (ValueError, IndexError):
            print("Невірний ввід! Спробуйте ще раз.")


# Основна функція гри
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        make_move(board, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Гравець {current_player} виграв!")
            break

        if check_draw(board):
            print_board(board)
            print("Нічия!")
            break

        # Перемикаємо гравця
        current_player = "O" if current_player == "X" else "X"


# Запуск гри
if __name__ == "__main__":
    play_game()
