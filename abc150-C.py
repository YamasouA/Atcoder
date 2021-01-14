from itertools import permutations

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

N = [i+1 for i in range(n)]

if p == q:
    print(0)
    exit()
for index, x in enumerate(permutations(N)):
    if x == p:
        pindex = index + 1
    elif x == q:
        qindex = index + 1
print(abs(pindex - qindex))