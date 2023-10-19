population = [int(x) for x in input().split(", ")]
min_wealth = int(input())

for i in range(len(population)):
    position_highest_value = population.index(max(population))
    if population[i] < min_wealth:
        population[position_highest_value] -= (min_wealth - population[i])
        population[i] += (min_wealth - population[i])

counter = 0
for i in population:

    if i < min_wealth:
        counter += 1

if counter == 0:
    print(population)
else:
    print( "No equal distribution possible")
