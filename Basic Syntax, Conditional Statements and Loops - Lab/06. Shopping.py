def shopping(budget):

    cost = 0

    while True:

        command = input()

        if command == "End":
            print("You bought everything needed.")
            break
        products = int(command)
        cost += products

        if cost > budget:
            print("You went in overdraft!")
            break

b = int(input())

shopping(b)