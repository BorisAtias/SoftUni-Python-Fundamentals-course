def factorial_division():

    factorial = int(input())
    divisioner = int(input())
    result = []
    final_result = 0

    for i in range(1, factorial):
        result.append(i)

    while len(result) > 0:
        final_result += factorial * result[-1]
        factorial = final_result
        final_result = 0
        result.pop()

    for i in range(1, divisioner):
        result.append(i)

    while len(result) > 0:
        final_result += divisioner * result[-1]
        divisioner = final_result
        final_result = 0
        result.pop()

    return (f'{factorial / divisioner:.2f}')

print(factorial_division())
