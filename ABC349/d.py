def calc(l, r):
    i = 0
    # l は 2^i * jである必要があるから 2^iで割り切れるかを見る
    while l % (2 ** i) == 0 and l + 2 ** i <= r:
        i += 1
    i -= 1
    return i

def main():
    l, r = map(int, input().split())

    ans = []
    while 1:
        i = calc(l, r)
        ans.append([l, l + 2 ** i])
        l += 2 ** i
        if l >= r:
            break
    print(len(ans))
    for a in ans:
        print(a[0], a[1])

if __name__ == "__main__":
    main()