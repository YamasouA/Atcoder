a, b, w = map(int, input().split())

m = 1000000000
M = 0

for i in range(1, 1000001):
    if a*i <= w*1000 and b*i >= w*1000:
        m = min(m, i)
        M = max(M, i)

if M == 0:
    print("UNSATISFIABLE ")
else:
    print(m, " ", M)