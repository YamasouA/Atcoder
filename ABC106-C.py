s = input()
k = int(input())

for i in range(k):
    if s[i] == '1':
        continue
    else:
        break

print(s[i])