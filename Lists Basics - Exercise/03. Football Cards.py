cards = input().split()

team_A = [1,2,3,4,5,6,7,8,9,10,11]
team_B = [1,2,3,4,5,6,7,8,9,10,11]

for _ in cards:

    element = _.split("-")
    team = element[0]
    player = int(element[1])

    if team == 'A':
        if player in team_A:
            team_A.remove(player)

    elif team == "B":
        if player in team_B:
            team_B.remove(player)

    if len(team_A) < 7 or len(team_B) < 7:
        break
print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")

if len(team_A) < 7 or len(team_B) < 7:
    print("Game was terminated")