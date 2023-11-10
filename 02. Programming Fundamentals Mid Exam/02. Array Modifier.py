nums = list(map(int, input().split()))

def swap():

    index1 = int(command[1])
    index2 = int(command[2])

    nums[index1], nums[index2] = nums[index2], nums[index1]

    return nums

def multiply():

    index1 = int(command[1])
    index2 = int(command[2])
    res = nums[index1] * nums[index2]
    del nums[index1]
    nums.insert(index1, res)

    return nums

def decrease():

    dec = [x - 1 for x in nums]
    return dec


while True:
    command = input().split()
    if command[0] == "end":
        print(*nums, sep=', ')
        break

    if command[0] == "swap":
        nums = swap()

    elif command[0] == "multiply":
        nums = multiply()

    elif command[0] == "decrease":
        nums = decrease()
