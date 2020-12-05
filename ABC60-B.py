a, b, c = map(int, input().split())

s = set()
find_flag = 0

for i in range(1, 100):
    rest = a * i % b
    if rest == c:
        find_flag = 1
        break
    if rest in s:
        break
    else:
        s.add(rest)

if find_flag:
    print("YES")
else:
    print("NO")