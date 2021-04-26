n = int(input())
a = list(map(int, input().split()))

now_m = 0
t_m = 0
for i in range(n):
    m = a[i]
    s = 0
    for j in range(n):
        if a[j] < m:
            if now_m < s:
                now_m = s
                s = 0
                continue
        else:
            s += m
    if now_m < s:
        now_m = s
    if t_m < now_m:
        t_m = now_m

print(now_m)
    