from functools import reduce
import math

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

n = int(input())
a = list(map(int, input().split()))

x = lcm(*a)
x -= 1

ans = 0
for i in range(n):
    ans += x % a[i]

print(ans)