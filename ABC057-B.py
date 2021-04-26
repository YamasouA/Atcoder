n, m = map(int, input().split())

ab = []
cd = []
ans = []

for i in range(n):
    x = list(map(int, input().split()))
    ab.append(x)

for j in range(m):
    x = list(map(int, input().split()))
    cd .append(x)

for i in range(n):
    d_min = 100000000000
    d_idx = -1
    for j in range(m):
        d = abs(ab[i][0]-cd[j][0]) + abs(ab[i][1] - cd[j][1])
        if d < d_min:
            d_min = d
            d_idx = j

    ans.append(d_idx)

for i in range(len(ans)):
    print(ans[i] + 1)