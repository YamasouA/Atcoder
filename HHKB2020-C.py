n = int(input())
p = list(map(int, input().split()))

L = [0] * 200002
s = 0

for i in range(n):
    L[p[i]] = 1
    while L[s]:
        s += 1
    print(s)