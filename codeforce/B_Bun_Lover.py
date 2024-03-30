import math

def fact(n):
    if n == 0:
        return 1
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def nPr(n, r):
    return fact(n) // fact(n - r)

def nCr(n, r):
    return fact(n) // (fact(r) * fact(n - r))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def mypow(a, b):
    ans = 1
    while b:
        if b & 1:
            ans *= a
        b //= 2
        a *= a
    return ans

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    n = int(input())
    print(n * (n + 1) + n + 2)

TC = int(input())
for _ in range(TC):
    solve()
