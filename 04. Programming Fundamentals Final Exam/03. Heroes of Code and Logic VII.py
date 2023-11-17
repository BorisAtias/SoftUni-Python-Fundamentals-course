def cast_spell(name, MP_needed, spell_name, heroes):
    if heroes[name]["MP"] >= MP_needed:
        heroes[name]["MP"] -= MP_needed
        print(f"{name} has successfully cast {spell_name} and now has {heroes[name]['MP']} MP!")
    else:
        print(f"{name} does not have enough MP to cast {spell_name}!")

    return heroes

def take_damage(name, damage, attacker, heroes):
    heroes[name]['HP'] -= damage
    if heroes[name]['HP'] > 0:
        print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['HP']} HP left!")
    else:
        print(f"{name} has been killed by {attacker}!")
        del heroes[name]

    return heroes

def recharge(name, MP_amount, heroes):
    curr_MP = heroes[name]["MP"]
    heroes[name]["MP"] += MP_amount
    if heroes[name]["MP"] > 200:
        heroes[name]["MP"] = 200
        print(f"{name} recharged for {200 - curr_MP} MP!")
    else:
        print(f"{name} recharged for {MP_amount} MP!")

    return heroes

def heal(name, HP_amount, heroes):
    curr_HP = heroes[name]["HP"]
    heroes[name]["HP"] += HP_amount
    if heroes[name]["HP"] > 100:
        heroes[name]["HP"] = 100
        print(f"{name} healed for {100 - curr_HP} HP!")
    else:
        print(f"{name} healed for {HP_amount} HP!")

    return heroes

def final_print(heroes):
    for hero, value in heroes.items():
        print(f"{hero}\n HP: {heroes[hero]['HP']}\n MP: {heroes[hero]['MP']}")


def heroes_of_code(n):
    heroes = {}
    for i in range(n):
        name, HP, MP = input().split()
        heroes[name] = {"HP": int(HP), "MP": int(MP)}

    while True:

        command = input().split(" - ")
        if command[0] == "End":
            final_print(heroes)
            break
        elif command[0] == "CastSpell":
            name, MP_needed, spell_name = command[1], int(command[2]), command[3]
            heroes = cast_spell(name, MP_needed, spell_name, heroes)
        elif command[0] == "TakeDamage":
            name, damage, attacker = command[1], int(command[2]), command[3]
            heroes = take_damage(name, damage, attacker, heroes)
        elif command[0] == "Recharge":
            name, MP_amount = command[1], int(command[2])
            heroes = recharge(name, MP_amount, heroes)
        elif command[0] == "Heal":
            name, HP_amount = command[1], int(command[2])
            heroes = heal(name, HP_amount, heroes)

n = int(input())

heroes_of_code(n)
