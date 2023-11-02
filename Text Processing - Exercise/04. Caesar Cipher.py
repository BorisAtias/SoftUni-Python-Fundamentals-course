text = input()

encrypted_text = ""

for i in text:
    i = ord(i) + 3
    encrypted_text += chr(i)
print(encrypted_text)