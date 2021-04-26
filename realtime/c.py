n = int(input())
lst = []
s = set()
for i in range(n):
    l = input()
    lst.append(l)
    s.add(l)
    
flag = True
for i in range(n):
    if '!' + lst[i] not in s:
        continue
    else:
        flag = False
        break

if flag:
    print("satisfiable")
else:
    print(lst[i])