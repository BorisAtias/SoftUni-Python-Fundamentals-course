password = input()

def check_pass():

    content = []

    for i in range(65, 90 + 1):
        content.append(chr(i))

    for j in range(97, 122 + 1):
        content.append(chr(j))

    num_content = []

    for num in range(48, 57 + 1):
        num_content.append(chr(num))

    l, char, digg = 0, 0, 0

    if len(password) < 6 or len(password) > 10:
        l += 1
        print("Password must be between 6 and 10 characters")

    if [x for x in password if x not in content and x not in num_content]:
        char += 1
        print("Password must consist only of letters and digits")

    if len([x for x in password if x.isdigit()]) < 2:
        digg += 1
        print("Password must have at least 2 digits")

    if l + char + digg == 0:
        print("Password is valid")


check_pass()
