def validate(password: str):
    if not (3 <= len(password) <= 16):
        return False
    for c in password:
        if not (c.isalnum() or c in ['-', '_']):
            return False
    return True


text = input().split(', ')

for name in filter(validate, text):
    print(name)

