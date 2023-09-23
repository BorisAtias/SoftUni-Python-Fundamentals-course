def Gryffindor(name):

    print(f"{name} goes to Gryffindor.")

def Slytherin(name):

    print(f"{name} goes to Slytherin.")

def Ravenclaw(name):

    print(f"{name} goes to Ravenclaw.")

def Hufflepuff(name):

    print(f"{name} goes to Hufflepuff.")

def Voldemort():

    print("You must not speak of that name!")


while True:
    counter = 0
    command = input()

    if command == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    elif command == "Voldemort":
        Voldemort()
        break

    elif len(command) < 5:
        Gryffindor(command)
    elif len(command) == 5:
        Slytherin(command)
    elif len(command) == 6:
        Ravenclaw(command)
    elif len(command) > 6:
        Hufflepuff(command)
