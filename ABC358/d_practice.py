n, m = map(int, input().split())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))
a_lst.sort()
b_lst.sort()
lst = []

a_idx, b_idx, total = 0, 0, 0
while b_idx < len(b_lst):
    if a_idx == len(a_lst):
        print(-1)
        exit()
    if b_lst[b_idx] <= a_lst[a_idx]:
        b_idx += 1
        total += a_lst[a_idx]
        lst.append(a_lst[a_idx])
    a_idx += 1
print(total)
