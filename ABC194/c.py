n = int(input())
A = list(map(int, input().split()))
dic = {}
for i in range(n):
    if A[i] not in dic:
        dic[A[i]] = 1
    else:
        dic[A[i]] += 1

ans = 0
for i in dic:
    for j in dic:
        ans += (i-j)**2 * dic[i] * dic[j]

print(ans//2)