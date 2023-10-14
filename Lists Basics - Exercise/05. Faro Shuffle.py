deck = input().split()
shuffles = int(input())

middle_index = len(deck) // 2

final_shuffle = []

for i in range(0, shuffles):
    final_shuffle = []

    for p in range(0, middle_index):

        final_shuffle.append(deck[p])
        final_shuffle.append(deck[middle_index])

        middle_index += 1
    deck = final_shuffle
    middle_index = len(deck) // 2

print(final_shuffle)
