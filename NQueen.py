answer = 0

def getNextNode(N, queens): 
	global answer
	if len(queens) >= N:
		return queens
	
	for newQueen in range(N):
		if isValid(N, queens, newQueen) == True:
			getNextNode(N, queens+[newQueen]) #O(n^n)
			answer = answer + 1

def isValid(N, queens, newQueen):
	#same column O(n)
	if newQueen in queens: 
		return False
	
	#same diagonal line O(n)
	y2 = len(queens)
	x2 = newQueen	
	y1 = 0
	for x1 in queens:
		if abs(x1-x2) == abs(y1-y2):
			return False
		y1 = y1+1
	return True

def printQueens(N, queens):
	for queen in queens:
		print('N'*(queen) + 'Q' + 'N'*(N-queen-1))
	print()

getNextNode(4, [])
print(answer)