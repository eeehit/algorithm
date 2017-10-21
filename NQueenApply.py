answer = 0
constraint = ["■■■□", "□□□□", "□■□□", "■■■□"]

def getNextNode(N, queens, y): 
	global answer
	if y >= N:
		print(queens)
		return
	
	for newQueen in range(N):
		if isValid(N, queens, newQueen, y) == True:
			getNextNode(N, queens+[newQueen], y+1) #O(n^n)
			answer = answer + 1

def isValid(N, queens, newQueen, y):
	global constraint
	if constraint[y][newQueen] == '■':
		return False
	
	#col check
	if newQueen in queens:
		return False
	
	return True

def printQueens(N, queens):
	for queen in queens:
		print('N'*(queen) + 'Q' + 'N'*(N-queen-1))
	print()

print(getNextNode(4, [], 0))