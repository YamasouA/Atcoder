n, s, d = map(int, input().split())
x = []
flag = False
for i in range(n):
    x.append(list(map(int, input().split())))
for i in range(n):
    if x[i][0] >= s:
        continue
    if x[i][1] <= d:
        continue
    flag = True
    break
if flag:
    print("Yes")
else:
    print("No")