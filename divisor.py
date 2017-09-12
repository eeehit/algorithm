import math

def divisorBasic(n):
	divisor = []
	i = 1
	while(i <= n):
		if n == 1:
			break;
		if n % i == 0:
			divisor.append(i)
		i = i+1
	return divisor

def divisorSqrt(n):
	divisor = []
	i = 1
	sqrt = math.sqrt(n)
	while(i<sqrt):
		if n == 1:
			break;
		if n%i == 0:
			divisor.append(i)
			divisor.append(int(n/i))
		i = i+1
	
	if pow(sqrt,2) == n:
		divisor.append(int(sqrt))
	
	return sorted(divisor)