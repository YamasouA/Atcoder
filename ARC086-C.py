from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))

lst = [0 for _ in range(n)]

for i in a:
    lst[i-1] += 1


lst.sort(reverse=True)
s = sum(lst[:k])
print(n-s)