import numpy as np
flag = True
n, w = map(int, input().split())
mat = [0 for _ in range(2*1000000)]
t_max = 0
for i in range(n):
    si, ti, pi = map(int, input().split())
    if t_max < ti:
        t_max = ti
    mat[si] += pi
    mat[ti] -= pi
    
cnt = 0
for i in range(t_max):
    cnt += mat[i]

    if cnt > w:
        flag = False
        break
if flag:
    print('Yes')
    
else:
    print('No')