n = int(input())
lst = list(map(int, input().split()))
x = 2 ** n
lst1 = lst[:x//2]
lst2 = lst[x//2:]


s1 = max(lst1)
s2 = max(lst2)

if s1 < s2:
    print(lst1.index(s1) + 1)
else:
    print(lst2.index(s2) + len(lst1) + 1)