from random import uniform


def InitGenome(min_val, max_val, length):
    return [uniform(min_val, max_val) for i in range(0,length)]
