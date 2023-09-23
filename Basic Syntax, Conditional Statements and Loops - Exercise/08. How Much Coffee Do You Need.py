def coffee_need():
    total = 0
    while True:

        command = input()
        if command == "END":
            if total <= 5:
                print(total)
            else:
                print("You need extra sleep")
            break
        elif "cat" in command or "CAT" in command or "dog" in command or "DOG" in command or "coding" in command or "CODING" in command or "movie" in command or "MOVIE" in command:
            if command.isupper():
                total += 2
            else:
                total += 1

coffee_need()
