n, m, t = map(int, input().split())
a, b = [], []
max_n = n

flag = True
for i in range(m):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

for i in range(m):
    if i == 0:
        n -= a[i]
    else:
        n -= a[i] - b[i-1]


    if n <= 0:
        flag = False
        break
    if n + b[i] - a[i] <= max_n:
        n += b[i] - a[i]
    else:
        n = max_n
     

if flag:
    n -= (t - b[-1])
    if n <= 0:
        print("No")
    else:
        print("Yes")
else:
    print("No")