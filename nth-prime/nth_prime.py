from math import log
def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    n = primes_range(number)
    prime = [True for i in range(n + 1)]
    out = []
    p = 2
    while(p * p <= n):
        if(prime[p] == True):
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p] == True:
            out.append(p)
    return out[number - 1]

def primes_range(number):
    x, p_x = 0, 0
    while p_x < number:
        x += 1000
        p_x = x/(log(x) - 1)
    return x