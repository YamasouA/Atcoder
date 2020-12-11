
n, m, x = map(int, input().split())
lst = []
for i in range(n):
    lsti = list(map(int, input().split()))
    lst.append(lsti)

small = 100000000000
flag = False

for i in range(1<<n):
    y = [0 for i in range(m)]
    cost = 0
    for j in range(n):
        if (i & (1 << j)):
            for k in range(m):
                y[k] += lst[j][k+1]
            cost += lst[j][0]

    if min(y) >= x:
        flag = True
        if small > cost:
            small = cost

if flag:
    print(small)

else:
    print("-1")