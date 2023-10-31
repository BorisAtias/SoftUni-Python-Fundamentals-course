import re

for demon in sorted(re.split(r", *", input())):
    demon = demon.strip()

    health_match = re.findall(r"[^\d\+\-*/\.]", demon)
    damage_match = re.findall(r"([-|+]?[\d+.\d]+)|([-|+]?[\d+])", demon)

    health = sum([ord(x) for x in health_match if x != "," and x.strip])
    damage = sum(float(x[0]) for x in damage_match)
    math_operation = re.findall(r"[\/\*]", demon)

    for operation in math_operation:
        if operation == "*":
            damage *= 2
        else:
            damage /= 2

    print(f"{demon} - {health} health, {damage:.2f} damage")
