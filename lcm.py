import gcd

def lcm(a,b):
	return a * b / gcd.euclideanIteration(a,b)