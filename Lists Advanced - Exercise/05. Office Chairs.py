rooms = int(input())
counter = 0
free_seats_counter = 0
for seats in range(1, rooms + 1):
    counter += 1

    chairs = input().split(' ')

    seats_available = len(chairs[0])
    guests = int(chairs[1])

    if seats_available < guests:
        print(f"{abs(seats_available - guests)} more chairs needed in room {counter}")
        free_seats_counter -= (guests - seats_available)
    else:
        free_seats_counter += seats_available - guests


if free_seats_counter >= 0:
    print(f"Game On, {free_seats_counter} free chairs left")