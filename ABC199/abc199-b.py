n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

max_a = 0
min_b = 10000

for i in range(n):
    if max_a < a[i]:
        max_a = a[i]
    if min_b > b[i]:
        min_b = b[i]
if min_b - max_a + 1 <= 0:
    print('0')
else:
    print(min_b - max_a + 1)