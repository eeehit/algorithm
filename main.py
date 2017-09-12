import random
import primeNumber
import divisor
import primeFactorization
import gcd
import lcm
import performanceCheck
import fibonacci

if __name__ == "__main__":
	#print(performanceCheck.testPrimeNumberIsPrimeBasic())
	#print(performanceCheck.testPrimeNumberIsPrimeSqrt())
	#print(performanceCheck.testDivisorDivisorBasic())
	#print(performanceCheck.testDivisorDivisorSqrt())	
	#print(performanceCheck.testGcdEuclideanRecursive())
	#print(performanceCheck.testGcdEuclideanIteration())
	#print(gcd.euclideanIteration(100,15))
	#print(gcd.euclideanRecursive(100,15))
	
	n = 20
	print(performanceCheck.testFibonacciRecursive(n))
	print(performanceCheck.testFibonacciMemo(n))
	print(performanceCheck.testFibonacciDynamicTable(n))
	print(performanceCheck.testFibonacciDynamicValue(n))
