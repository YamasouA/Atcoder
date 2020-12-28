s = input()
I = []
C = []
T = []
flag = False

for i in range(len(s)):
    if s[i] == 'c' or s[i] == 'C':
        C.append(i)
    elif s[i] == 't' or s[i] == 'T':
        T.append(i)
    elif s[i] == 'i' or s[i] == 'I':
        I.append(i)
if len(I) > 0 and len(T) > 0:
    for i in range(len(C)):
        if min(I) < C[i] and max(T) > C[i]:
            flag = True
            break

if flag:
    print("YES")
else:
    print("NO")