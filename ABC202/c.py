n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
dic = {}
for i in C:
    if B[i-1] not in dic:
        dic[B[i-1]] = 1
    else:
        dic[B[i-1]] += 1

ans = 0
for i in A:
    if i in dic:
        ans += dic[i]
print(ans)