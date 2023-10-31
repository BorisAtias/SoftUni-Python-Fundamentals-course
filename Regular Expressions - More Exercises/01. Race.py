import re

participants = input()

ranking = {}

while True:
    distance_sum = 0
    result = input()

    if result == "end of race":
        break

    name = re.findall(r"[a-zA-Z]", result)
    name = "".join(name)
    distance = re.findall(r"[0-9]", result)
    for i in distance:
        distance_sum += (int(i))

    if name in participants:
        if name not in ranking:
            ranking[name] = name
            ranking[name] = distance_sum
        else:
            ranking[name] += distance_sum
        distance_sum = 0
counter = 0
for key, value in sorted(ranking.items(), key=lambda val: val[1], reverse=True):
    if counter == 3:
        break
    else:
        counter += 1
        if counter == 1:
            print(f"{counter}st place: {key}")
        elif counter == 2:
            print(f"{counter}nd place: {key}")
        elif counter == 3:
            print(f"{counter}rd place: {key}")