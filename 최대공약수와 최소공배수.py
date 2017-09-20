#최대공약수와 최소공배수
#Level 1
#두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환해주는 gcdlcm 함수를 완성해 보세요. 배열의 맨 앞에 최대공약수, 그 다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 gcdlcm(3,12) 가 입력되면, [3, 12]를 반환해주면 됩니다.

#Python
def gcd(a, b):
	while(b != 0):
		tmp = a % b
		a = b
		b = tmp
	return a

def lcm(a, b, gcd):
	return int(a * b / gcd)

def gcdlcm(a,b):
    g = gcd(a,b)
    l = int(a * b / g)
    return [g,l]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(8,12))
