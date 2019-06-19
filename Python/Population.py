from .Individual import Individual

class Population(object):

    def __init__(self, popSettings):
        #function Evolved(genOld) - take old generation and return new one for
        #   next iteration
        self.Evolved = popSettings.NewGeneration 

        #function Log(newGen) - take set of individuals 
        #   and  return list of choosed characteristics
        self.Log = popSettings.Log

        #parameter Int - max ammount of generations to simulate
        self.maxGenerations = popSettings.maxGenerations

        #function StopCondition(genOld, genNew) - additional, generation specific
        #   condition, if none is required, return true
        self.ShouldContinue = popSettings.ShouldContinue


    def RunFor(popSize, indvSettings):
        oldGen = [Individual(indvSettings) for i in range(0,popSize)]
        Log(genOld)

        newGen = Evolved(genOld)
        Log(genNew)

        gen = 1
        while gen < maxGenerations and ShouldContinue(oldGen, newGen):
            oldGen = newGen
            newGen = Evolved(oldGen)
            Log(newGen)
    
