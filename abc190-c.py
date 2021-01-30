n, m = map(int, input().split())
jo = []
for i in range(m):
    jo.append(list(map(int, input().split())))

k = int(input())
sara = []
for i in range(k):
    sara.append(list(map(int, input().split())))
ans = []

max_cnt = 0
for i in range(0, 1<<k):
    s = set()
    cnt = 0
    for j in range(k):
        if i & (1 << j):
            s.add(sara[j][0])
           
        else:
            s.add(sara[j][1])
    #print(s)

    for l in range(m):
        if jo[l][0] in s and jo[l][1] in s:
            cnt += 1
       

    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)