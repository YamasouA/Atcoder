s = input()
ans = {}
for c in s:
    if c in ans:
        ans[c] += 1
    else:
        ans[c] = 1
a = [0 for i in range(1000)]
for k, v in ans.items():
    a[v] += 1

for i in a:
    if i != 0 and i != 2:
        print("No")
        exit()
print("Yes")