s = input()
t = input().lower()
i = 0
for c in s:
    if c == t[i]:
        i+=1
    if i == 3:
        break

if i ==3:
    print("Yes")
elif i == 2 and t[2] == 'x':
    print("Yes")
else:
    print("No")