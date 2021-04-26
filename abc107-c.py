h, w = map(int, input().split())

a = []
for i in range(h):
    a.append(list(input()))

idx_h = []
idx_w = []

for i in range(h):
    if a[i] == ['.'] * w:
        idx_h.append(i)
for j in range(w):
    
    for k in range(h):
        if a[k][j] == '.':
            if k == h-1:
                idx_w.append(j)
        else:
            break


ans = []
for i in range(h):
    lst = []
    if i in idx_h:
        continue
    for j in range(w):
        if j in idx_w:
            continue
        lst.append(a[i][j])
    ans.append(lst)

for i in range(len(ans)):
    lst = ''.join(ans[i])
    print(lst)
                
    