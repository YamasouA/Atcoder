n, l = map(int, input().split())

s = [input() for i in range(n)]

s_sort = sorted(s)

print(''.join(s_sort))