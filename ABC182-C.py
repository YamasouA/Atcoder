n = int(input())
ans=0
a1, a2, a0 = 0, 0, 0

while 1:
    x = n % 10
    a = int(x % 3)
    if a == 1:
        a1 += 1
    elif a == 2:
        a2 += 1
    else:
        a0 += 1
    n /= 10
    n = int(n)
    if x < 9:
        break

ans = (a1 + 2*a2) % 3
print(a1, a2, a0)
count = a1 + a2 + a0
if ans == 0:
    print('0')
elif ans  == 1:
    if (a1 > 0) and (count - 1 > 0):
        print('1')
    else:
        print('-1')

else:
    if (a2 > 0) and (count -1 > 0):
        print('1')
    elif (a1 >= 2) and (count - 2 > 0):
        print('2')
    else:
        print('-1')