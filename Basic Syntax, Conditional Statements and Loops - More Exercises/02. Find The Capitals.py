def find_the_capitals(string):

    result = [x for x, char in enumerate(string) if char.isupper()]

    print(result)

text = input()
find_the_capitals(text)