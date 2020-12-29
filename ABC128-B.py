n = int(input())
lst = []

for i in range(n):
    sp = list(input().split())

    lst.append([sp[0], -1*int(sp[1])])
ans = lst.copy()
lst.sort()


for i in range(n):
    for j in range(n):
        if lst[i] == ans[j]:
            print(j+1)
            break