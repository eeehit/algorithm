#괄호 확인하기
def is_pair(s):
    # 함수를 완성하세요
    check = []
    for i in s:
        if i == "(":
            check.append(i)
        elif i == ")":
            if not check:
                return False
            pop = check.pop()
            if pop == i:
                return False
    if check:
        return False
    return True


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( is_pair("(hello)()"))
print( is_pair(")("))
