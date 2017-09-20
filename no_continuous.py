#https://programmers.co.kr/learn/challenge_codes/86
def no_continuous(s):
    # 함수를 완성하세요
    answer = []
    
    if not s:
        return answer
    
    answer += s[0]
    for i in s:
        pop = answer.pop()
        if pop == i:
            answer += pop
        else:
            answer += pop + i
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))
