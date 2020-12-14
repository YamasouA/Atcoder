import collections

n = int(input())

s = []
for i in range(n):
    si = input()
    s.append(si)

for i in range(n):
    if i == 0:
        min = collections.Counter(s[i])
        continue
    else:
        c = collections.Counter(s[i])
    for keys in min:
        if keys not in c:
            min[keys] = 0
        if c[keys] < min[keys]:
            min[keys] = c[keys]
        else:
            pass

ans = ""
for keys in min:
    for i in range(min[keys]):
        ans += keys

lst = sorted(ans)
print(''.join(lst))