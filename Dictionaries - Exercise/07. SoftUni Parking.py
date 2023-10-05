cars = int(input())

parking_lot = {}

def register(username, number_plate):

    key = username
    value = number_plate

    if key in parking_lot.keys() and value != parking_lot[key] or key in parking_lot.keys() and value == parking_lot[key]:
        print(f"ERROR: already registered with plate number {parking_lot.get(key)}")
    else:
        parking_lot[key] = key
        parking_lot[key] = value
        print(f"{username} registered {value} successfully")


def unregister(username):

    key = username

    if key not in parking_lot.keys():
        print(f"ERROR: user {username} not found")
    else:
        parking_lot.pop(key)
        print(f"{username} unregistered successfully")


for i in range(cars):

    command = input().split()

    if command[0] == "register":
        register(command[1], command[2])

    if command[0] == 'unregister':
        unregister(command[1])

for key, value in parking_lot.items():
    print(f"{key} => {value}")
