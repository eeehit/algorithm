#count
#num1
#num2
#...
#num N
def input1():
	count = int(input())
	arr = []
	for i in range(count):
		number = int(input())
		arr.append(number)
	print(arr)

#count
#str1
#str2
#...
#str N
def input2():
	count = int(input())
	arr = []
	for i in range(count):
		str = input()
		arr.append(str)
	print(arr)

#str1 str2 ...str N
def input3():
	arr = input().split()
	print(arr)
	
#srt1, str2 static number of list
def input4():
	a, b = input().split()    # 입력받은 값을 공백을 기준으로 분리
	print(a)
	print(b)