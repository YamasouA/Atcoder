import math

def try_square_root_naive(n):
    m = int(math.sqrt(n))
    return abs(m*m - n) < 1e-6

s, p = map(int, input().split())

flag = False


if try_square_root_naive(s**2 - 4*p):
    print('Yes')

else:
    print('No')