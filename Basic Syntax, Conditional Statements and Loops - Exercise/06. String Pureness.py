def is_pure(string):

    if "," in string or "." in string or "_" in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")

count = int(input())

for i in range(count):
    text = input()
    is_pure(text)