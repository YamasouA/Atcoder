from collections import Counter
s = input()

cnt = Counter(s)
flag = True

if (cnt['S'] >= 1 and cnt['N'] >=1) or (cnt['S'] == 0 and cnt['N'] == 0): 
    if (cnt['E'] >= 1 and cnt['W'] >= 1) or (cnt['E'] == 0 and cnt['W'] == 0): 
        print("Yes")
        flag = False

if flag:
    print("No")