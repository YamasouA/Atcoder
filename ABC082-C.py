from collections import Counter
n = int(input())
a = list(map(int, input().split()))

numbers = Counter(a)

cnt = 0
for i in numbers:
    if numbers[i] == i:
        continue
    if i <= numbers[i]:
        cnt += (numbers[i] - i)
    else:
        cnt += numbers[i]


print(cnt)