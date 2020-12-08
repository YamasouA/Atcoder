w = input()
ans = ""
s = ["a", "i", "u", "e", "o"]
for i in range(len(w)):
    if w[i] in s :
        continue
    ans += w[i]

print(ans)
