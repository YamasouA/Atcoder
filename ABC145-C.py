import itertools
import math

n = int(input())
lst = []
for i in range(n):
    xy = list(map(int, input().split()))
    lst.append(xy)
dist = 0
for i, j in itertools.combinations(range(n), 2):
    dist += math.sqrt((lst[i][0] - lst[j][0])**2 + (lst[i][1] - lst[j][1])**2)

dist /= n

print(dist*2)
    