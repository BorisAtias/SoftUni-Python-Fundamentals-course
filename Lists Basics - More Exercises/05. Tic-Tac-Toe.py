def check_winner(field, player):
    # Check rows and columns for winnings
    for i in range(3):
        if all(cell == player for cell in field[i]) or all(field[j][i] == player for j in range(3)):
            return True

    # Check diagonals for winnings
    if all(field[i][i] == player for i in range(3)) or all(field[i][2 - i] == player for i in range(3)):
        return True

    return False


def main():
    field = [list(map(int, input().split())) for _ in range(3)]

    if check_winner(field, 1):
        print("First player won")
    elif check_winner(field, 2):
        print("Second player won")
    else:
        print("Draw!")


if __name__ == "__main__":
    main()
