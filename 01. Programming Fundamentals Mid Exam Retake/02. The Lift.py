def fill_lift(cabin_count, people):

    for cabin in range(len(cabin_count)):
        while cabin_count[cabin] < 4:
            cabin_count[cabin] += 1
            people -= 1
            if people == 0 and sum(cabin_count) / 4 == len(cabin_count):
                print(*cabin_count)
                break
            elif people == 0:
                print("The lift has empty spots!")
                print(*cabin_count)
                break
    return no_space(people, cabin_count)

def no_space(people, cabin_count):

    if people > 0:
        print(f"There isn't enough space! {people} people in a queue!")
        print(*cabin_count)


people_count = int(input())
lift_cabins = list(map(int, input().split()))
fill_lift(lift_cabins, people_count)