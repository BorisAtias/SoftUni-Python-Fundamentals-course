def sort():
    nums = input().split()

    host_list = []

    for i in nums:
        host_list.append(int(i))

    final_result = sorted(host_list)
    print(final_result)
sort()