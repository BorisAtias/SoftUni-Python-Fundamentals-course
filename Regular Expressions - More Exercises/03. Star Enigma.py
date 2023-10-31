import re

attack_A = []
attack_D = []
for _ in range(int(input())):
    text = input()
    key = len(re.findall(r"[star]", text.lower()))
    temp_str = ''
    for i in text:
        i = ord(i) - key
        temp_str += chr(i)

    pattern = r'@([A-Z][a-z]+)[^@\-!:>]*:\d+[^@\-!:>]*!(A|D)![^@\-!:>]*->\d+'
    match = re.findall(pattern, temp_str)
    if len(match) == 0:
        continue
    else:
        planet, attack_type = match[0][0], match[0][1]

        if attack_type == "A":
            attack_A.append(planet)
        else:
            attack_D.append(planet)

print(f"Attacked planets: {len(attack_A)}")

for planet in sorted(attack_A):
    print(f"-> {planet}")

print(f"Destroyed planets: {len(attack_D)}")

for planet in sorted(attack_D):
    print(f"-> {planet}")
