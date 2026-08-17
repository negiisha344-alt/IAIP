# Intern Alpha Internship
# Python Programming - Task 1
# Tic Tac Toe Game

def display_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for combination in winning_combinations:
        if (
            board[combination[0]] == player
            and board[combination[1]] == player
            and board[combination[2]] == player
        ):
            return True

    return False


def check_tie(board):
    return all(position in ["X", "O"] for position in board)


def play_game():
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    current_player = "X"

    print("\n===== TIC TAC TOE =====")
    print("Player 1: X")
    print("Player 2: O")
    print("Choose a position from 1 to 9.")

    while True:
        display_board(board)

        choice = input(
            f"Player {current_player}, enter your position (1-9): "
        )

        if not choice.isdigit():
            print("Invalid input! Please enter a number from 1 to 9.")
            continue

        position = int(choice)

        if position < 1 or position > 9:
            print("Invalid position! Choose a number from 1 to 9.")
            continue

        index = position - 1

        if board[index] in ["X", "O"]:
            print("That position is already taken. Choose another one.")
            continue

        board[index] = current_player

        if check_winner(board, current_player):
            display_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if check_tie(board):
            display_board(board)
            print("🤝 It's a tie!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


while True:
    play_game()

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("\nThank you for playing Tic Tac Toe!")
        break
