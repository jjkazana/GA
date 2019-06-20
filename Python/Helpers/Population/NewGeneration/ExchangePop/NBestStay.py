def NBestStay(newGen, oldGen, N):
	newGen.sort(key = lambda i : i.Adaptation, reverse=True)
	oldGen.sort(key = lambda i : i.Adaptation, reverse = True)

	return newGen[0: len(newGen)-N] + oldGen[0:N]
