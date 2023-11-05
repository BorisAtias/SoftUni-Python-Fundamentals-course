def add(piece, composer, key, collection):

    if piece not in collection:
        collection[piece] = {"Composer": composer, "Key": key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")


def remove_piece(piece, collection):

    if piece in collection:
        print(f"Successfully removed {piece}!")
        del collection[piece]
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key(piece, new_key, collection):

    if piece in collection.keys():
        collection[piece]["Key"] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def final_print(collection):
    for piece in collection.keys():
        print(f"{piece} -> Composer: {collection[piece]['Composer']}, Key: {collection[piece]['Key']}")


def the_pianist(piece_count):
    collection = {}
    for i in range(piece_count):

        piece, composer, key = input().split("|")
        collection[piece] = {"Composer": composer, "Key": key}

    while True:

        command = input().split("|")
        if command[0] == "Stop":
            final_print(collection)
            break
        elif command[0] == "Add":
            piece, composer, key = command[1], command[2], command[3]
            add(piece, composer, key, collection)
        elif command[0] == "Remove":
            piece = command[1]
            remove_piece(piece, collection)
        elif command[0] == "ChangeKey":
            piece, new_key = command[1], command[2]
            change_key(piece, new_key, collection)


piece_count = int(input())
the_pianist(piece_count)