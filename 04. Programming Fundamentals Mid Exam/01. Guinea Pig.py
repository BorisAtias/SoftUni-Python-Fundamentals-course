food_kg, hay_kg, cover_kg, puppy_weight_kg = [float(input()) * 1000 for _ in range(4)]

for days in range(1, 31):

    food_kg -= 300

    if days % 2 == 0:
        hay_kg -= (food_kg * 0.05)
    if days % 3 == 0:
        cover_kg -= (puppy_weight_kg / 3)

if food_kg <= 0 or hay_kg <= 0 or cover_kg <= 0:
    print("Merry must go to the pet store!")

else:
    print(f"Everything is fine! Puppy is happy! Food: {food_kg / 1000:.2f}, "
          f"Hay: {hay_kg / 1000:.2f}, "
          f"Cover: {cover_kg / 1000:.2f}.")