
def NotImplemented(Exeption):
    def __init__(self, function):
        self.value = function + ' is not implemented but used'

    def __str__(self):
        return repr("")


class IndvSettings(object):
    def __init__(self):
        self.Adaptation = None
        self.PreferenceFor = None
        self.InitGenome = None
        self.Cross = None

    def Fields(self):
        return ('Adaptation', 'PreferenceFor', 'InitGenome', 'Cross')

class Individual(object):

    def __init__(self, parent1, parent2):
        self.Adaptation = parent1.Adaptation
        self.PreferenceFor = parent1.PreferenceFor
        self.Cross = parent1.Cross
        self.Genome = Cross(parent1, parent2)


    def __init__(self, settings=IndvSettings())
        self.Adaptation = settings.Adaptation
        self.PreferenceFor = settings.PreferenceFor
        self.Genome = settings.InitGenome(length)
        self.Cross = settings.Cross

        if not self.Adaptation:
            raise NotImplemented('Adaptation()')
        if not self.PreferenceFor:
            raise NotImplemented('PreferenceFor(individual)')
        if not self.Genome:
            raise NotImplemented('InitGenome(length)')
        if not self.Cross:
            raise NotImplemented('Cross(indv1, indv2)')


    def CrossedWith(self, individual):
        return Individual(self, individual)

