def populations():
    population = {}
    population['Toronto'] = 5647656
    population['Ottawa'] = 1068821
    population['Kitchener'] = 522888
    population['London'] = 423369
    population['Hamilton'] = 729560
    return population

def sumPop(population):
    totalSum = 0
    for city, count in population.items():
        totalSum += count
    return totalSum

def minPop(population):
    smallest_pair = min(population.items())
    return smallest_pair[1]

def maxPop(population):
    largest_pair = max(population.items())
    return largest_pair[1]

def avgPop(population):
    totalSum = 0
    for city, count in population.items():
        totalSum += count
    avg = totalSum / len(population)
    return avg

def main():
    pop = populations()
    newList = []


    newList.extend([sumPop(pop), minPop(pop), maxPop(pop), avgPop(pop)])

    newList2 = []
    newList2.append(newList)

    print("Full structure:", newList2)
    print("Min Population:", newList2[0][1])
    print("Avg Population:", newList2[0][3])

if __name__ == '__main__':
    main()
