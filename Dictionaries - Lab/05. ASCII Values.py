my_string = input().split(", ")
values = {}

for i in my_string:
    key = i
    value = ord(i)
    values[key] = value

print(values)