employee_1_efficiency = int(input())
employee_2_efficiency = int(input())
employee_3_efficiency = int(input())

total_students = int(input())

answers_per_hour = employee_1_efficiency + employee_2_efficiency + employee_3_efficiency
count = 0
time = 0
while total_students > 0:
    if count == 3:
        count = 0
        time += 1
    else:
        count += 1
        time += 1
        total_students -= answers_per_hour

    if total_students <= 0:
        break

print(f"Time needed: {time}h.")