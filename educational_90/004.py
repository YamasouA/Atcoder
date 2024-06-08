def main():
    h, w = map(int, input().split())
    lsts = []
    for i in range(h):
        lsts.append(list(map(int, input().split())))
    sum_col = []
    sum_low = []
    for c in lsts:
        sum_low.append(sum(c))
    for l in zip(*lsts):
        sum_col.append(sum(l))
    for i in range(h):
        for j in range(w):
            print(sum_low[i] + sum_col[j] - lsts[i][j], end = ' ')
        print()

if __name__ == "__main__":
    main()