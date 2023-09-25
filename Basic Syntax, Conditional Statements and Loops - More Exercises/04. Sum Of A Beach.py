def sum_of_beach(string):

    result = string.count("water") + string.count("fish") + string.count("sand") + string.count("sun")

    print(result)

text = input().lower()

sum_of_beach(text)