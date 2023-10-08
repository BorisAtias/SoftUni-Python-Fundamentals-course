contests = {}

while True:
    command = input()
    if command == "end of contests":
        break

    tokens = command.split(":")
    key, value = tokens[0], tokens[1]
    contests[key] = key
    contests[key] = [value]

students = {}

while True:

    command = input()

    if command == "end of submissions":
        break

    tokens = command.split("=>")
    course, password = tokens[0], tokens[1]

    if course not in contests or password not in contests[course]:
        continue
    else:
        key, value = tokens[2], int(tokens[3])
        if key not in students:
            students[key] = key
            students[key] = {course:value}
        else:
            if course in students[key]:
                if students[key][course] >= value:
                    continue
                else:
                    students[key][course] = value
            else:
                students[key][course] = value
result = 0
best_candidate = ""
for student, points in students.items():

    if sum(points.values()) > result:
        result = sum(points.values())
        best_candidate = student
print(f"Best candidate is {best_candidate} with total {result} points.\nRanking:")

for student, contest in sorted(students.items()):
    print(student)
    for index in range(len(contest)):
        sorted_contest = sorted(contest.items(), key=lambda con: con[1], reverse=True)
        print(f"#  {sorted_contest[index][0]} -> {sorted_contest[index][1]}")
