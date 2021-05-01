n = int(input())
cnt_n = n
cnt = 0
ans = 0
while cnt_n != 0:
    cnt += 1
    cnt_n = cnt_n // 10
   

if cnt <= 3:
    pass

elif cnt <= 6:
    ans += n - 999

elif cnt <= 9:
    ans += (n - 999999) * 2
    ans += 999000

elif cnt <= 12:
    ans += (n-999999999) * 3
    ans += (999999999 - 999999) * 2
    ans += 999000

elif cnt <= 15:
    ans += (n-999999999999) * 4
    ans += (999999999999-999999999) * 3
    ans += (999999999 - 999999) * 2
    ans += 999000
else:
    ans += ((n-999999999999999) + (n-999999999999) + (n-999999999) + (n-999999) + (n-999))
print(ans)