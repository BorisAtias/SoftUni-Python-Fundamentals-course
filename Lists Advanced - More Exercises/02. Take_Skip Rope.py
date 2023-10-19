text = input()

letters = [letter for letter in text if not letter.isnumeric()]
nums = [int(x) for x in text if x.isnumeric()]

take_list = [nums[x] for x in range(len(nums)) if x % 2 == 0]
skip_list = [nums[x] for x in range(len(nums)) if x % 2 != 0]

take_string = ""
skip_string = ""
c = 0
for i in range(len(take_list)):
    for skip in skip_list:
        if c == len(take_list):
            break

        a = letters[0:take_list[i]]
        take_string += "".join(a)

        del letters[0:take_list[i]]
        del letters[0:skip]

        i += 1
        c += 1

print(take_string)
