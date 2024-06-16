n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input())

min_count = 999999999

for bit in range(1 << n):
    lst = ['x'] * m
    count = 0
    for i in range(n):
        if bit & (1 << i):
            count += 1
            for j in range(m):
                if s[i][j] == 'o':
                    lst[j] = 'o'
    if all(c == 'o' for c in lst):
        min_count = min(min_count, count)

# min_countが更新されていない場合、-1を返す
print(min_count)
