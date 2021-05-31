from decimal import Decimal 
def gcd(x, y):
    while x != 0 and y != 0:
        if x >= y:
            x = x % y
        else:
            y = y % x
    #print(x, y)
    return max(x, y)

a, b, c = map(Decimal, input().split())

ab = gcd(a, b)

r = gcd(ab, c)

ans = (a + b + c) / r - 3
print(int(ans))