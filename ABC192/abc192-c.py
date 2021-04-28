def fx(g1, g2):
    g1 = "".join(g1)
    g2 = "".join(g2)
    #print(g1, g2)
    g1_i = int(g1)
    g2_i = int(g2)
    return list(str(g2_i - g1_i))

if __name__ == "__main__":
    n, k = map(int, input().split())

    n = list(str(n))

    for i in range(k):
        g1 = sorted(n)
        g2 = sorted(n, reverse=True)

        n = fx(g1, g2)
    n = "".join(n)
    print(n)