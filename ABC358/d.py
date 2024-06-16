import bisect
n, m = map(int, input().split())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))
a_lst.sort()
b_lst.sort()

result = 0
pos = 0
for value in b_lst:
    # bisect_rightを使って、aの中でvalueより大きい最小の要素を見つける
    pos = bisect.bisect_left(a_lst, value, pos)
    if pos == len(a_lst):
        print("-1")
        exit()
    result += a_lst[pos]
    pos += 1
print(result)