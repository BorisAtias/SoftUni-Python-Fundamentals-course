def message(num):

    for i in range(num):

        code = int(input())

        if code == 88:
            print("Hello")
        elif code == 86:
            print("How are you?")
        elif code < 88 and code != 86:
            print("GREAT!")
        else:
            print("Bye.")

count = int(input())

message(count)