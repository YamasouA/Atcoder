n = int(input())
lst = []
for i in range(n):
    lst_i = list(map(int, input().split()))
    lst.append(lst_i)

lst = sorted(lst, key=lambda x:x[1])

for i in range(n):
    if lst[i][0]+0.5 < lst[i][2]:
        print(lst[i][1])
        exit()
print("-1")
    
