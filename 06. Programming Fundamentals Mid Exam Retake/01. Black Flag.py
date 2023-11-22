raid_duration = int(input())
plunder_per_day = int(input())
expected_plunder = float(input())

total_plundered = 0

for days in range(1, raid_duration + 1):

    total_plundered += plunder_per_day
    if days % 3 == 0:
        total_plundered += plunder_per_day * 0.5

    if days % 5 == 0:
        total_plundered *= 0.7

if total_plundered >= expected_plunder:
    print(f"Ahoy! {total_plundered:.2f} plunder gained.")
else:
    print(f"Collected only {(total_plundered / expected_plunder) * 100:.2f}% of the plunder.")

