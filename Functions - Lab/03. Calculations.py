operator = input()

num_1 = int(input())
num_2 = int(input())

def solve(a, b, operation):

    result = None

    if operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b
    elif operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    return result

print(int(solve(num_1, num_2, operator)))