from .Population import Population
from .Individual import Individual

from .Helpers.Population.Log.AvgAdapt import Log as AverageAdaptation
from .Helpers.Population.NewGeneration import *

from .Helpers.Individual.Cross.ProportionalBitwise import Cross as BitWise
from .Helpers.Individual.InitGenome.FloatInRange import InitGenome as FloatInRange
from .Helpers.Individual.PreferenceFor.SimilarityPercentageBetween import PreferenceFor as SimilarityPercentage


def Evolve(oldGen):
    newGen = []
    while len(newGen) < len(oldGen):
        p1 = MatchIndv.Tournament.FirstParentFrom(oldGen, 15)
        p2 = MatchIndv.Tournament.PartnerFor(p1, oldGen, 15)
        newGen.append(Individual(p1,p2))

    return newGen


popSettings = object()
popSettings.NewGeneration = Evolve
popSettings.Log = AverageAdaptation
popSettings.maxGenerations = 50
popSettings.Adaptation = 
popSettings.ShouldContinue = lambda x1,x2 : True



indvSettings = object()
indvSettings.InitGenome = FloatInRange
indvSettings.Cross = BitWise
indvSettings.PreferenceFor = SimilarityPercentage


def Run():

    pop = Population(popSettings)
    res = pop.RunFor(100, indvSettings)

    for line in res:
        print(line)
