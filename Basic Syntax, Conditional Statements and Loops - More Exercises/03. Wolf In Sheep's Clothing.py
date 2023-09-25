def sheep_wolfe(string):

    if string.pop() == 'wolf':
        print("Please go away and stop eating my sheep")
        raise SystemExit
    string = string[::-1]
    for spot, animal in enumerate(string):
        if animal != "sheep":
            print(f"Oi! Sheep number {spot + 1}! You are about to be eaten by a wolf!")

text = input().split(", ")

sheep_wolfe(text)