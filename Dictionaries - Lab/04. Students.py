def create_dict(name, id, course, students):
    students[id] = {name: course}

    return students


def print_massive(command, students):
    if "_" in command:
        command = command.replace("_", " ")
    for key, value in students.items():
        for name, course in value.items():

            if course == command:
                print(f"{name} - {key}")


massive = {}

while True:

    command = input()

    if ":" not in command:
        print_massive(command, massive)
        break

    tokens = command.split(":")

    name = tokens[0]
    student_id = tokens[1]
    course = tokens[2]
    massive = create_dict(name, student_id, course, massive)
