num_students = int(input())

score_cards = {}

for i in range(num_students):

    name = input()
    score = float(input())

    key = name
    value = score
    if key not in score_cards:
        score_cards[key] = key
        score_cards[key] = [value]
    else:
        score_cards[key].append(value)

for key, j in score_cards.items():

    value = sum(j) / len(j)
    score_cards[key] = value

for key, value in list(score_cards.items()):

    if value < 4.50:
        score_cards.pop(key)

for key, value in score_cards.items():
    print(f"{key} -> {value:.2f}")