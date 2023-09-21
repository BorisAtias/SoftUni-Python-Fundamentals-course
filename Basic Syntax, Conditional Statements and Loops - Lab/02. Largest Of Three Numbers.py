# First way

def largest_of_tree(a,b,c):

    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)

num1 = int(input())
num2 = int(input())
num3 = int(input())

largest_of_tree(num1,num2,num3)

# Second way

n1 = int(input())
n2 = int(input())
n3 = int(input())
print(max(n1, n2, n3))
