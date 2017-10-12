# -*- coding: utf-8 -*-

# 어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
# 예를 들어 d(91) = 9 + 1 + 91 = 101
# 이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.
# 어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
# 그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.
# 예를 들어 1, 3, 5, 7, 9, 20, 31 은 셀프 넘버 들이다.
# 1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.


def d(generator, loopcnt):
    number = generator
    sum = 0
    while(number>0):
        sum += number % 10
        number = number // 10
        loopcnt += 1
    return (sum+generator, loopcnt)

# 에라토스테네스의 체의 아이디어를 차용해서, 루프를 돌면서 selfNumber만 남긴다
def selfNumberList(n):
    loopcnt = 0
    arr = list(range(1, n))
    for generator in range(1, n):
        (result, loopcnt) = d(generator, loopcnt)
        if result > n:
            break;
        if result in arr:
            arr.remove(result)
    #print loopcnt
    return arr

# 에라토스테네스의 체의 아이디어를 차용해서, 루프를 돌면서 selfNumber만 남기는데,
# d(1) = d(0) + (2*1) 인 점을 활용해서 d(n) 함수를 1/10 만큼만 돌린다.
def selfNumberList2(n):
    loopcnt = 0
    result = 0
    arr = list(range(1, n))
    for generator in range(1, n):
        if generator % 10 is 0:
            (result,loopcnt) = d(generator,loopcnt)
            if result > n:
                break;
            if result in arr:
                arr.remove(result)
        else:
            result += 2
            if result > n:
                break;
            if result in arr:
                arr.remove(result)
    #print loopcnt
    return arr

print sum(selfNumberList(5000))
print sum(selfNumberList2(5000))