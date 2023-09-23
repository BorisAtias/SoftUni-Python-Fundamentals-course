def transform_strings(str1, str2):
    temp_str = list(str1)

    for i in range(len(str2)):

        if str2[i] != str1[i]:
            temp_str[i] = str2[i]
            transformed_str = "".join(temp_str)
            print(transformed_str)


string1 = input()
string2 = input()
transform_strings(string1, string2)
