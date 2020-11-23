n, x = map(int, input().split())
s = input()

for i in range(n):
    if s[i] == 'o':
        x += 1
    elif s[i] == 'x':
        if x == 0:
            continue
        else:
            x -= 1

print(x)