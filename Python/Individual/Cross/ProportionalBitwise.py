from random import randint

def Cross(i1, i2):
    newGenome = []
    for i in range(0,len(i1.Genome)):
        #float bits
        sl1ce = randint(0,64)
        a = (~float(0)) >> sl1ce
        g1 = i1.Genome[i]
        g2 = i2.Genome[i]
        #preserve bits from 1 most significant to sl1ce from g1
        #   and rest from g2
        newGenome.append( (g1&(~a)) | (g2&a) )
        
    return newGenome
