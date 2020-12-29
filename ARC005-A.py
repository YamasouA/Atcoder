n = int(input())
w = list(input().split())
w[-1] = w[-1].replace(".", "")

ans_lst = ["TAKAHASHIKUN", "Takahashikun", "takahashikun"]

cnt = 0
for i in range(n):
    if w[i] in ans_lst:
        cnt += 1

print(cnt)