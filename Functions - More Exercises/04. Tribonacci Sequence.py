def tribonacci(num):
    result = [1]
    for i in range(num - 1):
        if len(result) > 3:
            result.append(sum(result[len(result) - 1: len(result) - 4: -1]))
        else:
            result.append(sum(result))
    return result

number = int(input())
print(*tribonacci(number), sep=" ")