def num_1_100():

    while True:
        num = float(input())
        if num < 1 or num > 100:
            continue
        else:
            print(f"The number {num} is between 1 and 100")
            break
num_1_100()


