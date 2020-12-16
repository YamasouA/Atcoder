n, t = map(int, input().split())

a = []
for i in range(n):
    a.append(int(input()))

time = 0
for i in range(n):
    if i == 0:
        continue
    if t > a[i] - a[i-1]:
        time += a[i] - a[i-1]
    else:
        time += t

time += t

print(time)