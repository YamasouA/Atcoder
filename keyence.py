n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = []
max_a = 0
for i in range(n):
    if i == 0:
        c.append(a[0]*b[0])
        max_a = a[0]
    else:
        max_a = max(max_a, a[i])
        c.append(max(c[i-1], max_a*b[i]))
    print(c[i])
        