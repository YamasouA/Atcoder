def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    divi = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            divi.append(i + n//i)
        i += 1
    return divi

n = int(input())

lst = make_divisors(n)

min = 100000000000000
for i in range(len(lst)):
    dist = lst[i] - 2
    if dist < min:
        min = dist

print(min)