n = int(input())
h = list(map(int, input().split()))

flag = True
for i in range(n):
    if i == 0:
        continue
    if h[i]-1 >= h[i-1]:
        h[i] -= 1
    elif h[i-1] > h[i]:
        flag = False
        break
    else:
        continue

if flag:
    print("Yes")
else:
    print("No")