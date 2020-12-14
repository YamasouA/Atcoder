from math import factorial
l = int(input())

ans = factorial(l-1) // (factorial(11) * factorial(l-1-11))
print(ans)
