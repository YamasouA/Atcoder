a, b = map(int, input().split())

sa = 0
sb = 0
for i in range(3):
    sa += a % 10 
    a = a // 10

for i in range(3):
    sb += b % 10 
    b = b // 10

if sb > sa:
    print(sb)
else:
    print(sa)