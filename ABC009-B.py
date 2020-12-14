n = int(input())
a = []
for i in range(n):
    ai = int(input())
    a.append(ai)
max = 0
second = 0

for i in range(n):
    if a[i] > max:
        second = max
        max = a[i]
    elif (a[i] > second) and (a[i] != max):
        second = a[i]

print(second)