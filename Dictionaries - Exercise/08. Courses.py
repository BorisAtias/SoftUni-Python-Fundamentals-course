courses = {}

while True:
    command = input()

    if command == "end":
        break

    command = command.split(" : ")

    course = command[0]
    user = command[1]

    if course not in courses:
        courses[course] = course
        courses[course] = [user]
    else:
        courses[course].append(user)

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for name in value:
        print(f"-- {name}")