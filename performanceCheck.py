import threading
import time
import random
import primeNumber
import divisor
import primeFactorization
import gcd
import lcm
import fibonacci

def start():
	return time.time()

def end(start):
	timer = time.time()-start
	return timer

def average(values):
  if len(values) == 0:
    return None
  return sum(values, 0.0) / len(values)

def printLog(func, average):
	return ("[%s]\t%f" % (func, average))

def testPrimeNumberIsPrimeBasic():
	count = []
	for i in range(1,100):
		n = random.randrange(2, 100)
		start_time = start()
		primeNumber.isPrimeBasic(n)
		count.append(end(start_time))
	return printLog("primeNumber.isPrimeBasic", average(count))

def testPrimeNumberIsPrimeSqrt():
	count = []
	for i in range(1,100):
		n = random.randrange(2, 100)
		start_time = start()
		primeNumber.isPrimeSqrt(n)
		count.append(end(start_time))
	return printLog("primeNumber.isPrimeSqrt", average(count))

def testDivisorDivisorBasic():
	count = []
	for i in range(1,100):
		n = random.randrange(2, 100)
		start_time = start()
		divisor.divisorBasic(n)
		count.append(end(start_time))
	return printLog("divisor.divisorBasic", average(count))

def testDivisorDivisorSqrt():
	count = []
	for i in range(1,100):
		n = random.randrange(2, 100)
		start_time = start()
		divisor.divisorSqrt(n)
		count.append(end(start_time))
	return printLog("divisor.divisorSqrt", average(count))

def testGcdEuclideanRecursive():
	count = []
	a = random.randrange(2, 100)
	b = random.randrange(2, a)
	for i in range(1,100):
		start_time = start()
		gcd.euclideanRecursive(a, b)
		count.append(end(start_time))
	return printLog("gcd.euclideanRecursive", average(count))

def testGcdEuclideanIteration():
	count = []
	a = random.randrange(2, 100)
	b = random.randrange(2, a)
	for i in range(1,100):
		start_time = start()
		gcd.euclideanIteration(a, b)
		count.append(end(start_time))
	return printLog("gcd.euclideanIteration", average(count))

def testFibonacciRecursive(n):
	count = []
	start_time = start()
	print(fibonacci.recursive(n))
	return printLog("fibonacci.recursive", end(start_time))

def testFibonacciMemo(n):
	count = []
	start_time = start()
	print(fibonacci.memo(n))
	return printLog("fibonacci.recursive", end(start_time))

def testFibonacciDynamicTable(n):
	count = []
	start_time = start()
	print(fibonacci.dynamicTable(n))
	return printLog("fibonacci.dynamicTable", end(start_time))

def testFibonacciDynamicValue(n):
	count = []
	start_time = start()
	print(fibonacci.dynamicValue(n))
	return printLog("fibonacci.dynamicValue", end(start_time))