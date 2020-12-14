import math

n, m = map(int, input().split())
if m > 0:
    a = list(map(int, input().split()))
    a.sort()
    s = []
    if a[0] -1 != 0:
        s.append(a[0]-1)
    for i in range(1, m):
        ax = a[i]-a[i-1]-1
        if ax == 0:
            continue
        s.append(ax)
    al = n - a[-1]
    if al != 0:
        s.append(al)
  
    if len(s) != 0:
        x = min(s)
        cnt = 0
        for i in range(len(s)):
            cnt += math.ceil(s[i] / x)
        print(cnt)
    else:
        print("0")



else:
    print("1")
