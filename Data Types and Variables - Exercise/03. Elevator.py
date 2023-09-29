from math import ceil

num_of_people = int(input())
elevator_capacity = int(input())

print(ceil(num_of_people / elevator_capacity))