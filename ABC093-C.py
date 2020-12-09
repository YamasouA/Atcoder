abc = list(map(int, input().split()))

cnt = 0
while True:
    abc.sort()
    if (abc[0] == abc[1]) and (abc[1] == abc[2]):
        break
    if abc[1] == abc[2]:
        abc[0] += 2
        cnt += 1
    else:
        abc[0] += 1
        abc[1] += 1
        cnt += 1

    

print(cnt)