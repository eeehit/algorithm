#가장 큰 정사각형 찾기
#Level 4
#O와 X로 채워진 표가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다. 표에서 O로 이루어진 가장 큰 정사각형을 찾아 넓이를 반환하는 findLargestSquare 함수를 완성하세요. 예를 들어
#1	2	3	4	5
#X	O	O	O	X
#X	O	O	O	O
#X	X	O	O	O
#X	X	O	O	O
#X	X	X	X	X
#가 있다면 정답은
#1	2	3	4	5
#X	O	O	O	X
#X	O	O	O	O
#X	X	O	O	O
#X	X	O	O	O
#X	X	X	X	X
#가 되며 넓이는 9가 되므로 9를 반환해 주면 됩니다.

def findLargestSquare(board):
    
    def archive(board):
        l = len(board)
        for i in range(0,l-1):
            for j in range(0,l-1):
                if board[i][j] == 'O' and board[i][j+1] == 'O' and board[i+1][j] == 'O' and board[i+1][j+1]:
                    board[i][j] = 'O'
                else :
                    board[i][j] = 'X'
        for i in range(0,l):
            del(board[i][-1])
        return board[:-1]
    
    def checkEnd(board):
        l = len(board)
        count = 0
        for i in range(0,l):
            for j in range(0,l):
                if board[i][j] == 'O':
                    count += 1
        return count
    
    answer = 0
    while(len(board) > 1) :
        count = checkEnd(board)
        if count >= 1:
            answer += 1
        if count <= 1:
        	break;
        board = archive(board)
    return (answer)**2

#아래 코드는 출력을 위한 테스트 코드입니다.

testBoard = [['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O']]
print(findLargestSquare(testBoard))


#
def findLargestSquare(board):
    answer = 1
    res = [[1 if x=='O' else 0 for x in y] for y in board]
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 'O':
                res[y][x] = min(res[y-1][x], res[y-1][x-1], res[y][x-1]) + 1
                if res[y][x] > answer: answer = res[y][x]

    return answer ** 2

#아래 코드는 출력을 위한 테스트 코드입니다.

testBoard = [['X','O','O','O','X'],['X','O','O','O','O'],['X','X','O','O','O'],['X','X','O','O','O'],['X','X','X','X','X']]
print(findLargestSquare(testBoard))
