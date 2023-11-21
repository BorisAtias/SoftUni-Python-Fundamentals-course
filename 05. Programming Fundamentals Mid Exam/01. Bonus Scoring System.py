students_count = int(input())
total_lectures = int(input())
additional_bonus = int(input())

bonus_max, attendance_max = 0, 0

for bonus in range(students_count):

    attendance = int(input())

    total_bonus = attendance / total_lectures * (5 + additional_bonus)

    if attendance > attendance_max:
        attendance_max = attendance

    if total_bonus > bonus_max:
        bonus_max = total_bonus

print(f"Max Bonus: {round(bonus_max)}.")
print(f"The student has attended {attendance_max} lectures.")