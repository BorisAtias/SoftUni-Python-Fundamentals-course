sub_strings = list(input().split(", "))
strings = list(input().split())

result = []
for el in sub_strings:
    for i in strings:
        if el in i:
            result.append(el)

final_result = []
[final_result.append(x) for x in result if x not in final_result]
print(final_result)