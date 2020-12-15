n, m = map(int, input().split())
lst = []

for i in range(n):
    ai, bi = map(int, input().split())
    lst.append([ai, bi])
lst.sort()

c = 0
for i in range(n):
    if m > lst[i][1]:
        c += lst[i][0] * lst[i][1]
        m -= lst[i][1] 
    else:
        c += lst[i][0] * m
        m = 0
    if m == 0:
        print(c)
        break