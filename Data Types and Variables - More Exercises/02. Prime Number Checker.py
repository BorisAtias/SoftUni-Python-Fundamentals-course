num = int(input())
i = 2
prime = True

while i <= num / 2:

    rem = num % i

    if rem != 0:
        i = i + 1
    else:
        prime = False
        break
print(prime)