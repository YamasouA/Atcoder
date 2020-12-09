n = int(input())

lst = []
num = 0
idx = 0
max = 0
for i in range(n):
    lsti = list(input().split())
    lsti[1] = int(lsti[1])
    lst.append(lsti)
    num += lsti[1]
    if max < lsti[1]:
        idx = i
        max = lsti[1]
if num / 2 < max:
    print(lst[idx][0])
else:
    print("atcoder")