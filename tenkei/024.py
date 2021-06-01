n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
flag = False
for i in range(n):
    cnt += abs(A[i]-B[i])
    if cnt > k:
        print("No")
        exit()

A_sum = 0
B_sum = 0
for i in range(n):
    A_sum += A[i]
    B_sum += B[i]

if A_sum % 2 == B_sum % 2:
    if k%2 == 0:
        flag = True

elif A_sum % 2 != B_sum %2:
    if k%2 != 0:
        flag = True

if flag:
    print("Yes")
else:
    print("No")