def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


n = int(input())
x = make_divisors(2*n)
cnt = 0
for i in range(len(x)):
    j = n / x[i]
    if j % 2 == 0:
        continue
    else:
        cnt += 1
print(cnt)