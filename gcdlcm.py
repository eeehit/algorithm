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
