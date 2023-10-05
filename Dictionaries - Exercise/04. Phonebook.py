contact = input()
phonebook = {}

while len(contact) > 1:
    text = contact.split("-")

    key = text[0]
    value = text[1]
    phonebook[key] = key
    phonebook[key] = value

    contact = input()

if len(contact) == 1:
    contact = int(contact)

for i in range(contact):

    contact = input()

    if contact not in phonebook.keys():
        print(f"Contact {contact} does not exist.")
    else:
        print(f"{contact} -> {phonebook[contact]}")