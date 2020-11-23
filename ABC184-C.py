import math
def search(r1, c1, r2, c2):
    count = 0
    if (r1+c1) == (r2+c2):
        return 1
    elif (r1-c1) == (r2-c2):
        return 1
    elif (abs(r1-r2)+abs(c1-c2) <= 3):
        return 1
    
    return count + search()

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
if r1 == r2 and c1 == c2:
    ans = 0

elif (r1+c1) == (r2+c2):
    ans = 1
elif (r1-c1) == (r2-c2):
    ans = 1
elif (abs(r1-r2)+abs(c1-c2) <= 3):
    ans = 1

elif (r1+r2+c2-c1)%2 == 0:
    ans = 2

elif abs((c2 - c1 + r1) - r2) <= 3:
    ans = 2

elif abs((r1 + c1 - c2) - r2) <= 3:
    ans = 2

else:
    ans = 3
print(ans)