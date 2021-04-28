r, x, y = map(int, input().split())

dist = x**2 + y**2
dist = dist**0.5

x_now = 0
y_now = 0
cnt = 0
flag = False
if dist == r:
    print(cnt+1)
    exit()
while dist > 2*r:
    x_now = x_now + x * r / ((x**2 + y**2)**0.5)  
    y_now = y_now + y * r / ((x**2 + y**2)**0.5)
    cnt += 1
    dist = (x-x_now)**2 + (y-y_now)**2
    dist = dist**0.5
    #print(x_now, y_now, dist)

print(cnt+2)