a, b, k = map(int, input().split())

if a >= k:
    a -= k
    print("{} {}".format(a, b))
else:
    k -= a
    a = 0
    b -= k
    if b < 0:
        b = 0
    print("{} {}".format(a, b))