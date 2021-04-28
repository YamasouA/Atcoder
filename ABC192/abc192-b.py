s = input()

for i in range(len(s)):
    if i % 2 == 1:
        if s[i].islower():
            print("No")
            exit()
    else:
        if s[i].isupper():
            print("No")
            exit()
print("Yes")