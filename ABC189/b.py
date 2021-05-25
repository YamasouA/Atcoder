n, x = map(int, input().split())
vp = []
for i in range(n):
    vpi = list(map(int, input().split()))
    vp.append(vpi)

now = 0
for i in range(n):
    now += vp[i][0] * vp[i][1]
    if now > x*100:
        print(i+1)
        exit()
print("-1")