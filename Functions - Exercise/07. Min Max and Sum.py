def min_max():
    nums = input().split()

    host_list = []

    for i in nums:
        host_list.append(int(i))

    print(f"The minimum number is {min(host_list)}")
    print(f"The maximum number is {max(host_list)}")
    print(f"The sum number is: {sum(host_list)}")
min_max()