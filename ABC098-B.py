n = int(input())
s = input()

res = 0
for i in range(1, n-1):
    x = set(s[:i])
    y = set(s[i:])
    tmp = len(x.intersection(y))
    res = max(res, tmp)
    
print(res)