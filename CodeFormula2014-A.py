a, b = map(int, input().split())

p = list(map(int, input().split()))
q = list(map(int, input().split()))

ans = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]

if a > 0:
    for i in p:
        ans[i] = "."
if b > 0:
    for i in q:
        ans[i] = "o"


print(ans[7]," ", ans[8], " ", ans[9], " ", ans[0])
print(" ", ans[4], " ", ans[5], " ", ans[6])
print(" ", " ", ans[2], " ", ans[3])
print(" ", " ", " ", ans[1])
