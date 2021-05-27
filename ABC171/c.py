n = int(input())
ans = ""
moji = 'a'
moji_n = 96
while n > 0:
    n -= 1
    amari = int(n % 26) 

    ans = chr(ord(moji) + amari) + ans
    #ans += chr(moji_n + amari)
    n /= 26
    n = int(n)
    if n == 0:
        break

print(ans)
