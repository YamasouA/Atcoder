a, b, c = map(int, input().split())

a2 = a*a
b2 = b*b
c2 = c*c

if a2 + b2 < c2:
    print("Yes")

else:
    print("No")