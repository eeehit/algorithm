import math

def primeFactorization(n):
    prime = []
    
    i = 2
    sqrt = math.sqrt(n)
    
    while(i<=sqrt):
        if n == 1:
            break;
        if n%i == 0:
            n = n/i
            prime.append(i)
        else:
            i = i+1
    return prime
