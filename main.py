import random
import primeNumber
import divisor
import primeFactorization
import gcd
import lcm
import performanceCheck

if __name__ == "__main__":
	print(performanceCheck.testPrimeNumberIsPrimeBasic())
	print(performanceCheck.testPrimeNumberIsPrimeSqrt())
	print(performanceCheck.testDivisorDivisorBasic())
	print(performanceCheck.testDivisorDivisorSqrt())	
	print(performanceCheck.testGcdEuclideanRecursive())
	print(performanceCheck.testGcdEuclideanIteration())
	print(gcd.euclideanIteration(100,15))
	print(gcd.euclideanRecursive(100,15))