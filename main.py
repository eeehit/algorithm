import random
import primeNumber
import divisor
import primeFactorization
import gcd
import lcm
import performanceCheck

if __name__ == "__main__":
	n = random.randrange(2, 100)
	#m = random.randrange(2, n-1)
	print(performanceCheck.testPrimeNumberIsPrimeBasic(n))
	print(performanceCheck.testPrimeNumberIsPrimeSqrt(n))
	print(performanceCheck.testDivisorDivisorBasic(n))
	print(performanceCheck.testDivisorDivisorSqrt(n))	
	print(performanceCheck.testGcdEuclideanIteration(100,15))
	print(performanceCheck.testGcdEuclideanRecursive(100,15))
	
	print(gcd.euclideanIteration(100,15))
	print(gcd.euclideanRecursive(100,15))