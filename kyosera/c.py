n = int(input())
a = list(map(int, input().split()))

dic = {}
for i in range(n):
    amari = a[i] % 200
    if amari not in dic.keys():
        dic[amari] = 1
    else:
        dic[amari] += 1
ans = 0
for i in dic:
    ans += (dic[i] * (dic[i]-1)) / 2

print(int(ans))