n = int(input())
n_sq = int(n ** 0.5)
s = set()

for i in range(2, n_sq+1):
    x = i ** 2
    while x <= n:
        s.add(x)
        x *= i
print(n - len(s))