n = int(input())
lst = []
a = 0

for i in range(n):
    ax, tx = map(int, input().split())
    x = 2 * ax + tx
    lst.append([x, ax, tx])
    a += ax

lst.sort(reverse=True)

cnt = 0
num = 0
for i in range(n):
    num += lst[i][1] + lst[i][2]
    cnt += 1

    if num > (a-lst[i][1]):
        flag = True
        break
    else:
        a -= lst[i][1]
if flag:
    print(cnt)