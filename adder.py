#두 정수 사이의 합
def adder(a, b):
    # 함수를 완성하세요
    n = min(a,b)
    m = max(a,b)
    return int((n+m) * (m-n+1) / 2)
