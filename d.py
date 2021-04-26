dp = [[[-1 for _ in range(101)] for _ in range(101)] for _ in range(101)]
a, b, c = map(int, input().split())
for i in range(99, 0, -1):
    for j in range(99, 0, -1):
        for k in range(99, 0, -1):
            if (i+j+k == 0):
                continue
            ans = 0
            ans += dp[i+1][j][k]*i
            ans += dp[i][j+1][k]*j
            ans += dp[i][j][k+1]*k
            dp[i][j][k] = ans / (i+j+k) + 1

print(dp[a][b][c])