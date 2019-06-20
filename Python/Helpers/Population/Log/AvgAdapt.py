
def Log(population):
    avg = 0.0
    for indv in population:
        avg += indv.Adaptation/len(population)

    return avg
