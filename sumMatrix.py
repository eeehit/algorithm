import numpy as np
def sumMatrix(A,B):
    answer = np.array(A) + np.array(B)
    return answer.tolist()

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))
