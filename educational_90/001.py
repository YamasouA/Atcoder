n, length = map(int, input().split())
k = int(input())
lst = list(map(int, input().split()))


def solve(m):
    tmp = 0
    cnt = 0
    for i in range(n):
        if lst[i] - tmp >= m and length - lst[i] >= m:
            cnt += 1
            tmp = lst[i]
    return cnt >= k
r = length
l = 0
while r - l > 1:
    mid = (r + l) // 2
    is_solve = solve(mid)
    if is_solve:
        l = mid
    else:
        r = mid
print(l)