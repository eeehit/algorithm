#약수의 합
#Level 1
#어떤 수를 입력받아 그 수의 약수를 모두 더한 수 sumDivisor 함수를 완성해 보세요. 예를 들어 12가 입력된다면 12의 약수는 [1, 2, 3, 4, 6, 12]가 되고, 총 합은 28이 되므로 28을 반환해 주면 됩니다.

import math
def sumDivisor(num):
    answer = 0
    sqrt = int(math.sqrt(num))
    i = 1
    
    while(i<sqrt):
        if num == 1:
            break;
        if num%i == 0:
            answer += (i + int(num/i))
        i = i+1
        
    if pow(sqrt,2) == num:
        answer += int(sqrt)
        
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumDivisor(12))
