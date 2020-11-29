a, b, x, y = map(int, input().split())
time = 0
if (2 * x < y) and (a < b):
    time = abs(a - b) * 2 * x + x
elif (2 * x < y) and (a > b):
    time = abs(a - b - 1) * 2 * x + x
elif a > b:
    time = (a - b - 1) * y + x
elif a == b:
    time = x
elif a < b:
    time = (b - a) * y + x

print(time)