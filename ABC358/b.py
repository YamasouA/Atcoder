n, a = map(int, input().split())
t = list(map(int, input().split()))
sum = t[0] + a
print(sum)
stack = list()
for i in range(1, len(t)):
    if t[i] < sum:
        sum += a
    else:
        sum = t[i] + a
    print(sum)