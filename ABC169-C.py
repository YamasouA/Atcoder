import math

a, b = input().split()
a = int(a)
b = float(b)

b = b * 100

x = a * b
x //= 100
ans = int(math.floor(x))
print(ans)