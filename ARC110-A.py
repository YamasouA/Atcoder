import math
from functools import reduce

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

n = int(input())
lst = []
for i in range(2, n+1, 1):
    lst.append(i)
x = lcm(*lst)

ans = 10000000000000 % x
if ans == 0:
    ans = 1000000000000 - ans + 1
else: 
    ans = 10000000000000 - ans + 1

print(ans)