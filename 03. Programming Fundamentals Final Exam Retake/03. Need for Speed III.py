def drive(car, distance, fuel, garage):
    if fuel > garage[car]["Fuel"]:
        print("Not enough fuel to make that ride")
    else:
        garage[car]["Fuel"] -= fuel
        garage[car]["Mileage"] += distance
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if garage[car]["Mileage"] >= 100000:
            print(f"Time to sell the {car}!")
            del garage[car]

    return garage


def refuel(car, fuel, garage):
    curr_tank = garage[car]["Fuel"]
    garage[car]["Fuel"] += fuel
    if garage[car]["Fuel"] > 75:
        garage[car]["Fuel"] = 75
        print(f"{car} refueled with {75 - curr_tank} liters")
    else:
        print(f"{car} refueled with {fuel} liters")

    return garage


def revert(car, kilometers, garage):
    garage[car]["Mileage"] -= kilometers
    print(f"{car} mileage decreased by {kilometers} kilometers")
    if garage[car]["Mileage"] < 10000:
        garage[car]["Mileage"] = 10000

    return garage


def final_print(garage):
    for car, value in garage.items():
        print(f"{car} -> Mileage: {garage[car]['Mileage']} kms, Fuel in the tank: {garage[car]['Fuel']} lt.")


def create_garage(n):
    garage = {}

    for i in range(n):
        car, mileage, fuel = input().split("|")
        garage[car] = {"Mileage": int(mileage), "Fuel": int(fuel)}

    while True:

        command = input().split(" : ")
        if command[0] == "Stop":
            final_print(garage)
            break
        elif command[0] == "Drive":
            car, distance, fuel = command[1], int(command[2]), int(command[3])
            garage = drive(car, distance, fuel, garage)
        elif command[0] == "Refuel":
            car, fuel = command[1], int(command[2])
            garage = refuel(car, fuel, garage)
        elif command[0] == "Revert":
            car, kilometers = command[1], int(command[2])
            garage = revert(car, kilometers, garage)

n = int(input())
create_garage(n)
