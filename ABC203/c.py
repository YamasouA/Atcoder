n, k = map(int, input().split())


ab = []
for i in range(n):
    a_i, b_i = map(int,input().split())

    ab.append([a_i, b_i])
ab = sorted(ab, key=lambda x: x[0])

stay = 0

for i in range(len(ab)):

    cost = ab[i][0] - stay
    if cost > k:
        print(stay + k)
        exit()
    k -= cost
    k += ab[i][1]
    stay = ab[i][0]

if k >= 0:
    print(ab[-1][0]+k)
else:
    print(ab[-1][0])