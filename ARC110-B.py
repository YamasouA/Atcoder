n = int(input())
t = input()

if t in "110"*(10**5):
    if t == "11":
        print(10**10)
    elif t == "1":
        print(2*(10**10))
    else:
        cnt = 0
        for i in range(n):
            if t[i] == "0":
                cnt += 1
        if t[-1] == "0":
            print((10**10)-cnt+1)
        else:
            print((10**10)-cnt)

else:
    print('0')