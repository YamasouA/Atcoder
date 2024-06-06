c_lst = ["(", ")"]

def rec_write(lst, n, cnt):
    if cnt < 0:
        return
    if n == 0 and cnt == 0:
        for c in lst:
            print(c, end='')
        print()
    if n == 0:
        return
    else:
        for c in c_lst:
            lst.append(c)
            rec_write(lst, n-1, cnt + 1 if c == "(" else cnt - 1)
            lst.pop()
    

if __name__ == "__main__":
    n = int(input())
    lst = []
    if n % 2 != 0:
        exit
    else:
        rec_write(lst, n, 0)
