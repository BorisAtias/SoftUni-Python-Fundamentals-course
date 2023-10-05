courses = {}

while True:
    command = input()

    if command == "End":
        break

    command = command.split(" -> ")

    company = command[0]
    user_id = command[1]
    if company in courses and user_id in courses[company]:
        continue
    elif company not in courses:
        courses[company] = company
        courses[company] = [user_id]
    else:
        courses[company].append(user_id)

for key, value in courses.items():
    print(f"{key}")
    for name in value:
        print(f"-- {name}")
