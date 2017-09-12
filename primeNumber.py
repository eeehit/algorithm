import math

#소수 판별법 - 나머지가 0인 수 검사
def isPrimeBasic(n):
	for i in range(2, n-1):
		if n % i == 0:
			return False
	return True

#소수 판별법 - 제곱근 이용
def isPrimeSqrt(n):
	sqrt = int(math.sqrt(n))+1
	for i in range(2, sqrt):
		if n % i == 0:
			return False
	return True

#에라토스테네스의 체
def EratosthenesSiev(n):
	p=2
	arr = list(range(1, n))
	
	while(pow(p,2) < n):
		for i in arr:
			if i%p == 0 and i is not p:
				arr.remove(i)
		p = p+1
	return arr