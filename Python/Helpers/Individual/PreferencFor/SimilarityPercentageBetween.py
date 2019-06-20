from numpy.random import normal

gaussTable = normal(32,10, 128)
def Preference(i1,i2):
    ret = 0
    for i in range(0,len(i1.Genome)):
        ret += bin(i1.Genome[i] & i2.Genome[i]).count('1')

    return gaussTable[int(ret/len(i1.Genome))]

