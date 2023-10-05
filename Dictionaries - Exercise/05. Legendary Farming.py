base_holder = []

elements = {'shards': 0, 'fragments': 0, 'motes': 0}

shards, fragments , motes = 0, 0, 0

while True:
    if shards >= 250 or fragments >= 250 or motes >= 250:
        break

    inventory = input().lower().split()

    for i in inventory:

        if i.isdigit():
            i = int(i)
            base_holder.append(i)
        else:
            base_holder.append(i)

    while len(base_holder) != 0:

        key = base_holder[1]
        value = base_holder[0]

        if key not in elements:
            elements[key] = key
            elements[key] = value
            base_holder.pop(0)
            base_holder.pop(0)
        else:
            elements[key] += value
            base_holder.pop(0)
            base_holder.pop(0)

        a, b, c = elements.get("shards"), elements.get("fragments"), elements.get("motes")
        if a >= 250 or b >= 250 or c >= 250:
            if a >= 250:
                shards += a
                a -= 250
                elements['shards'] -= 250
                print("Shadowmourne obtained!")
            elif b >= 250:
                fragments += b
                b -= 250
                elements['fragments'] -= 250
                print("Valanyr obtained!")
            elif c >= 250:
                motes += c
                elements['motes'] -= 250
                print("Dragonwrath obtained!")
            break

for key, value in elements.items():
    print(f"{key}: {value}")
