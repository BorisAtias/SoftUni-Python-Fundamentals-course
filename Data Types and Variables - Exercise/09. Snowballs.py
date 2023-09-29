count = int(input())
weight = 0
curr_time = 0
curr_quality = 0
best_value = 0
for balls in range(count):

    ball_weight = int(input())
    time_to_make = int(input())
    quality = int(input())

    ball_value = (ball_weight / time_to_make) ** quality
    if ball_value > best_value:
        weight = ball_weight
        curr_time = time_to_make
        best_value = ball_value
        curr_quality = quality

print(f"{weight} : {curr_time} = {int(best_value)} ({curr_quality})")