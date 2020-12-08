n = int(input())
max = 2025

x =  max - n

for i in range(1, 10):
    for j in range(1, 10):
        if i * j == x:
            print(i, " x ", j)