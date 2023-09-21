def even_numbers(n):

    for i in range(n):
        num = int(input())
        if not num % 2 == 0:
            print(f"{num} is odd!")
            break
    else:
        print("All numbers are even.")

count = int(input())

even_numbers(count)