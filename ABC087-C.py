n = int(input())

a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

lst1 = []
lst2 = []

for i in range(n):
    if i == 0:
        lst1.append(a1[0])
        lst2.append(a2[0])
    else:
        sum1 = lst1[i-1] + a1[i]
        sum2 = lst2[i-1] + a2[i]
        
        lst1.append(sum1)
        lst2.append(sum2)

max = 0
for i in range(n):
    x = lst1[i] + lst2[n-1] - lst2[i] + a2[i]
    if x > max:
        max = x

print(max)