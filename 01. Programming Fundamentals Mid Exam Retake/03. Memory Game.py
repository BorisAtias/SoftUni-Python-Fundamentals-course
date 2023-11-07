def find_pairs(element_1, element_2, board):
    print(f"Congrats! You have found matching elements - {board[element_1]}!")
    if element_1 > element_2:
        board.pop(element_1)
        board.pop(element_2)
    else:
        board.pop(element_2)
        board.pop(element_1)


def new_elements(counter, position, board):
    extra_elements = str(-counter) + "a"
    board.insert(position, extra_elements)
    board.insert(position, extra_elements)
    print("Invalid input! Adding additional elements to the board")


def try_again():
    print("Try again!")


def loose(board):
    print("Sorry you lose :(")
    print(*board)


def win(counter):
    print(f"You have won in {counter} turns!")


pairs = input().split()
moves_count = 0

while len(pairs) > 1:

    picks = input()
    if picks == "end":
        loose(pairs)
        break
    commands = picks.split()

    index_1 = int(commands[0])
    index_2 = int(commands[1])
    middle = int(len(pairs) / 2)
    moves_count += 1

    if index_1 not in range(len(pairs)) or index_2 not in range(len(pairs)) or index_1 == index_2:
        new_elements(moves_count, middle, pairs)
        continue
    if pairs[index_1] != pairs[index_2]:
        try_again()
        continue
    if pairs[index_1] == pairs[index_2]:
        find_pairs(index_1, index_2, pairs)

if len(pairs) <= 1:
    win(moves_count)
