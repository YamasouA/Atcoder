n = int(input())
s = input()
ans = []

for i in range(n):
    ans.append(s[i])
    print(len(ans))
    print(ans[-3:])
    while len(ans) >= 3:
        if ans[-3:] == ['f', 'o', 'x']:
            ans = ans[:-3]
        else:
            break
print(len(ans))
