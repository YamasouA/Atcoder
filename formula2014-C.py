s = input()
ans = []
for i in range(len(s)-1):
    if s[i] == '@':
        if 'a' <= s[i+1] and s[i+1] <= 'z':
            for j in range(1,len(s)-i):
                if 'a' <= s[i+j] and s[i+j] <= 'z':
                    flag = True
                    continue
                else:
                    flag = False
                    break
            if flag:
                add = s[i+1:i+j+1]
            else:
                add = s[i+1:i+j]
            if add not in ans:
                ans.append(add)

ans.sort()
for i in range(len(ans)):
    print(ans[i])
                