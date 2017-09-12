arr_memo = [0]*(50+1)

def recursive(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return recursive(n-1) + recursive(n-2)

def memo(n):
	if n == 0:
		arr_memo[0] = 0
		return 0
	elif n == 1:
		arr_memo[1] = 1
		return 1
	else:
		arr_memo[n] = recursive(n-1) + recursive(n-2)
		return arr_memo[n]

def dynamicTable(n):
	arr = [0]*(n+1)
	arr[0] = 0
	arr[1] = 1
	for i in range(2,n+1):
		arr[i] = arr[i-1] + arr[i-2]
	return arr[n]

def dynamicValue(n):
	a = 0
	b = 1
	for i in range(2,n+1):
		c = a+b
		a = b
		b = c
	return c