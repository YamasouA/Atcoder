n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(input())
ans = 9999999999
for bit in range(1 << n):
    count = 0
    check = [False] * m
    # それぞれの行がbitに対応しているかを確認する
    for i in range(n):
        if bit & (1 << i):
            count += 1
            for j in range(m):
                if lst[i][j] == 'o':
                    check[j] = True
        if all(c for c in check):
            ans = min(ans, count)
print(ans)