from random import sample

def FirstParentFrom(population,k):
    candidates = sample(population,k)

    ret = candidates[0]
    for indv in candidates:
        if ret.Adaptation < indv.Adaptation:
            ret = indv

    return ret

def PartnerFor(i, population,k):
    candidates = sample(population,k)
    
    ret = candidates[0]
    tmpAdapt = ret.Adaptation * i.PreferenceFor(ret)

    for indv in candidates:
        if i.PreferenceFor(indv)*indv.Adaptation > tmpAdapt:
            tmpAdapt = i.PreferenceFor(indv)*indv.Adaptation
            ret = indv
    
    return ret
