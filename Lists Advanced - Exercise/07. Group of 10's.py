nums = [int(x) for x in input().split(", ")]

groups = 0

while nums:

    groups += 10

    curr_group = list(filter(lambda x: x <= groups, nums))
    for el in curr_group:
        nums.remove(el)

    print(f"Group of {groups}'s: {curr_group}")