import itertools
n = int(input())
lst = []
for i in range(n):
    x, y = map(int, input().split())
    lst.append([x, y])
count = 0
for i, j in itertools.combinations(range(n), 2):
    grad = (lst[i][1] - lst[j][1]) / (lst[i][0] - lst[j][0])
    if grad <= 1 and grad >= -1:
        count += 1
print(count)