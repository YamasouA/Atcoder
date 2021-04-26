n = int(input())
s = list(input())
q = int(input())
tab = []
for i in range(q):
    query = list(map(int, input().split()))
    tab.append(query)

bef = s[:n]
aft = s[n:]

for i in range(q):
    if tab[i][0] == 1:
        if tab[i][1]-1 < n and tab[i][2]-1 < n:
            buf = bef[tab[i][1]-1]
            bef[tab[i][1]-1] = bef[tab[i][2]-1]
            bef[tab[i][2]-1] = buf
        elif tab[i][1]-1 < n and tab[i][2]-1 >= n:
            buf = bef[tab[i][1]-1]
            bef[tab[i][1]-1] = aft[tab[i][2]-n-1]
            aft[tab[i][2]-n-1] = buf
        elif tab[i][1]-1 >= n:
            buf = aft[tab[i][1]-n-1]
            aft[tab[i][1]-n-1] = aft[tab[i][2]-n-1]
            aft[tab[i][2]-n-1] = buf
    else:
        buf = aft
        aft = bef
        bef = buf

    #print(i, bef, aft)

s = bef + aft
ans = "".join(s)
print(ans)