def is_win(game):
    # Check rows and columns
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != ' ':  # Check row i
            return True
        if game[0][i] == game[1][i] == game[2][i] != ' ':  # Check column i
            return True

    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] != ' ':  # Check main diagonal
        return True
    if game[0][2] == game[1][1] == game[2][0] != ' ':  # Check anti-diagonal
        return True

    return False


def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
    player1 = 'X'
    player2 = 'O'
    turn = False  # False for player 1's turn, True for player 2's turn. Player 1 first.
    print("X = Player 1")
    print("O = Player 2")
    for n in range(9):  # Maximum 9 moves
        turn = not turn  # Switch turns
        current_player = player1 if not turn else player2
        print(f"Player {1 if not turn else 2}: Which cell to mark? i:[1..3], j:[1..3]: ")

        while True:  # Loop until valid input is provided
            try:
                i, j = map(int, input().split())  # Get user input
                i -= 1  # Convert to 0-based index
                j -= 1  # Convert to 0-based index

                # Check if input is within valid range
                if i < 0 or i >= 3 or j < 0 or j >= 3:
                    print("Invalid input! Coordinates must be between 1 and 3. Try again.")
                    continue

                # Check if the cell is already occupied
                if game[i][j] != ' ':
                    print("This cell is already occupied! Choose another one.")
                    continue

                # If everything is fine, break the loop
                break
            except ValueError:  # Handle non-integer input
                print("Invalid input! Please enter two integers separated by a space. Try again.")

        # Update the game board
        game[i][j] = current_player

        # Check if the current player has won
        if is_win(game):
            print(f"Player {1 if not turn else 2} wins!")
            break  # Terminate the game

        # Show the game board
        for row in game:
            print(" ".join(row))

    else:  # If the loop completes without breaking, it's a tie
        print("Tie game!")


if __name__ == "__main__":
    main()
