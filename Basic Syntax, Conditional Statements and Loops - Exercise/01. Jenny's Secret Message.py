def greet_all(text):

    name = text

    print(f"Hello, {name}!")

def greet_Johnny():

    print(f"Hello, my love!")


text = input()
if text == "Johnny":
    greet_Johnny()
else:
    greet_all(text)