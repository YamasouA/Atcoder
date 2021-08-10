h, w, n = map(int, input().split())
a = list()
b = list()
for i in range(n):
    a_i, b_i = map(int, input().split())
    a.append(a_i)
    b.append(b_i)
#座標圧縮
#重複を省くためにlist -> set -> listで変換する
xdic = {x: i+1 for i, x in enumerate(sorted(list(set(a))))}
ydic = {y: i+1 for i, y in enumerate(sorted(list(set(b))))}

for i in range(n):
    print(xdic[a[i]], ydic[b[i]])