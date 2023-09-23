def easter_bread(budget, flower):
    pack_of_eggs = flower * 0.75
    milk_L = flower * 1.25

    loaf_cost = flower + pack_of_eggs + (milk_L * 0.25)
    loafs_made = 0
    colored_eggs = 0
    while budget >= loaf_cost:

        budget -= loaf_cost
        loafs_made += 1
        colored_eggs += 3
        if loafs_made % 3 == 0:
            colored_eggs -= (loafs_made - 2)

    print(f"You made {loafs_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

budget = float(input())
flower = float(input())

easter_bread(budget,flower)