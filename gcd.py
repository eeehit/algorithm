def euclideanRecursive(a, b):
	if (a % b == 0) and (a > b):
		return b
	return euclideanRecursive(b, a % b)

def euclideanIteration(a, b):
	while(b != 0):
		tmp = a % b
		a = b
		b = tmp
	return a