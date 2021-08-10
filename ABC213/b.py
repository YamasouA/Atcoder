n = int(input())
a = list(map(int, input().split()))

second = 0
first = 0
idx_f = 0
idx_s = 0
for i in range(n):
    if (first < a[i]):
        second = first
        first = a[i]
        idx_s = idx_f
        idx_f = i + 1
    elif (second < a[i]):
        second = a[i]
        idx_s = i + 1
    #print("first: {}, second: {}, a[i]: {}, {}".format(first, second, a[i], i))
    
print(idx_s)