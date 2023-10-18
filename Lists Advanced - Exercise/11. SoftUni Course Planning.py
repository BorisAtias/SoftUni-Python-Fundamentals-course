def add(lesson, schedule):
    if lesson not in schedule:
        schedule.append(lesson)

    return schedule


def insert(index, lesson, schedule):
    if not lesson in schedule:
        schedule.insert(index, lesson)

    return schedule


def remove(lesson, schedule):
    index = schedule.index(lesson)
    if index + 1 == f"{lesson}-Exercise":
        schedule.pop(schedule[lesson] + 1)

    schedule.remove(lesson)

    return schedule


def swap(lesson1, lesson2, schedule):
    exercise1 = ""
    exercise2 = ""
    for el in range(len(schedule)):
        if schedule[el] == lesson1:
            schedule[el] = lesson2
            if el + 1 in range(len(schedule)) and schedule[el + 1] == f"{lesson1}-Exercise":
                exercise1 += schedule[el + 1]
                schedule.remove(exercise1)
        elif schedule[el] == lesson2:
            schedule[el] = lesson1
            if el + 1 in range(len(schedule)) and schedule[el + 1] == f"{lesson2}-Exercise":
                exercise2 += schedule[el + 1]
            if len(exercise1) > 0:
                schedule.insert(el + 1, exercise1)
        if schedule[el] == exercise2:
            schedule.remove(exercise2)
            if len(exercise2) > 0:
                for i in range(len(schedule)):
                    if schedule[i] == lesson2:
                        schedule.insert(i + 1, exercise2)

    return schedule


def exercise(lesson, schedule):
    if lesson in schedule and f"{lesson}-Exercise" not in schedule:
        lesson_index = schedule.index(lesson)
        schedule.insert(lesson_index + 1, f"{lesson}-Exercise")
    elif lesson not in schedule:
        schedule.append(lesson)
        schedule.append(f"{lesson}-Exercise")

    return schedule


def final_print(schedule):

    for index, value in enumerate(schedule):
        print(f"{index + 1}.{value}")


schedule = input().split(", ")

while True:

    command = input().split(":")

    if command[0] == "course start":
        final_print(schedule)
        break

    elif command[0] == "Add":
        lesson = command[1]
        schedule = add(lesson, schedule)
    elif command[0] == "Insert":
        lesson, index = command[1], int(command[2])
        schedule = insert(index, lesson, schedule)
    elif command[0] == "Remove":
        lesson = command[1]
        if lesson in schedule:
            schedule = remove(lesson, schedule)
    elif command[0] == 'Swap':
        lesson1, lesson2, = command[1], command[2]
        if lesson1 in schedule and lesson2 in schedule:
            schedule = swap(lesson1, lesson2, schedule)
    elif command[0] == "Exercise":
        lesson = command[1]
        schedule = exercise(lesson, schedule)

