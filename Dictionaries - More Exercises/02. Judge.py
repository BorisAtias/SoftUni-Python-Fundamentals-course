contests = {}

while True:
    command = input()

    if command == "no more time":
        break

    command = command.split(" -> ")

    name, course, points = command[0], command[1], int(command[2])

    if course not in contests:
        contests[course] = {name: points}
    elif name not in contests[course]:
        contests[course][name] = points
    elif points > contests[course][name]:
        contests[course][name] = points

final_points = {}

for course, students in contests.items():
    counter = 0
    print(f"{course}: {len(students)} participants")

    sorted_points = sorted(students.items(), key=lambda x: (-x[1], x[0]))

    for index, (student, points) in enumerate(sorted_points, start=1):
        counter += 1
        print(f"{counter}. {student} <::> {points}")

        if student not in final_points:
            final_points[student] = points
        else:
            final_points[student] += points

sorted_final_points = sorted(final_points.items(), key=lambda x: (-x[1], x[0]))

print("Individual standings:")

for index, (student, points) in enumerate(sorted_final_points, start=1):
    print(f"{index}. {student} -> {points}")
