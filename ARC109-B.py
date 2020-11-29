import math
n = int(input())

s = 0
e = n + 1

while e-s > 1:
    m = (s+e) // 2

    if m*(m+1) // 2 <= n+1:
        s = m
    else:
        e = m

print(n+1-s)