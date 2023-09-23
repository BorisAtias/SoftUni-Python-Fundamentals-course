def drink_somth(age):

    if age <= 14:
        print("drink toddy")
    elif age <= 18:
        print("drink coke")
    elif age <= 21:
        print("drink beer")
    else:
        print("drink whisky")

text = int(input())

drink_somth(text)