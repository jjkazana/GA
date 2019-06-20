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

		#function for calculating indv Adaptation from given Genome, see indvSettings.InitGenome
        self.Adaptation = popSettings.Adaptation


    def RunFor(popSize, indvSettings):
        resume = []
        
        oldGen = [Individual(indvSettings) for i in range(0,popSize)]
        for indv in oldGen:
            indv.Adaptation = self.Adaptation(indv.Genome)
        resume.append(Log(genOld))

        newGen = Evolved(genOld)
        for indv in newGen:
            indv.Adaptation = self.Adaptation(indv.Genome)
        resume.append(Log(genNew))

        gen = 1
        while gen < maxGenerations and ShouldContinue(oldGen, newGen):
            oldGen = newGen
            newGen = Evolved(oldGen)
            for indv in newGen:
                indv.Adaptation = self.Adaptation(indv.Genome)
            resume.append(Log(newGen))

        return resume
