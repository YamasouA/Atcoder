from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
cnt = Counter(a)
print(cnt)
bef = -1
for i in cnt:
    if i == bef+1:
        bef = i
        if cnt[i] < k:
            ans += cnt[i] * i
            k -= cnt[i]
            
            if k == 0:
                break

    else:
        ans += cnt[i] * i
        break

print(ans)
