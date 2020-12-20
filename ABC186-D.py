import numpy as np
n = int(input())
a = list(map(int, input().split()))

ans = 0
x = 0
a.sort()
for i in range(1, n):
    ans += a[i] * i
    ans -= a[i-1] * (n-i)

print(ans)