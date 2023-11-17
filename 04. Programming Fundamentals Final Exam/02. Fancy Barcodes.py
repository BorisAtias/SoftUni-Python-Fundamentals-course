import re

count = int(input())

coco = []
for i in range(count):

    text = input()

    pattern = r"((@)(#{1,})([A-Z]([A-Za-z0-9]{4,})[A-Z])(@)(#{1,}))"
    matches = re.finditer(pattern, text)
    coco.append(matches)
    for match in matches:
        key = match.group(1)
        coco.append(key)
    if len(coco) <= 1:
        print("Invalid barcode")
        coco.clear()
    else:
        coco.pop(0)
        for code in coco:
            nums = ""
            for char in code:
                if char.isnumeric():
                    nums += char

            if nums == "":
                print(f"Product group: {'00'}")
            else:
                print(f"Product group: {nums}")
                nums = ""
        coco.clear()
