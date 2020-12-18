s = input()
t = input()
lst = ["a", "t", "c", "o", "d", "e", "r", "@"]
flag = True
for i in range(len(s)):
    if s[i] == "@":
        if t[i] in lst:
            continue
        else:
            flag = False
            break
    elif t[i] == "@":
        if s[i] in lst:
            continue
        else:
            flag = False
            break
    elif s[i] == t[i]:
        continue
    else:
        flag = False
        break

if flag:
    print("You can win")

else:
    print("You will lose")