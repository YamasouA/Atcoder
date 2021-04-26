n = int(input())
a = list(map(int, input().split()))

flag = True
ans = 1
if 0 in a:
    ans = 0
else:
    for i in range(n):
        ans *= a[i]
        if ans > 10**18:
            flag = False
            break
if flag:
    print(ans)
else:
    print('-1')