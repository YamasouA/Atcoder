from collections import Counter
def main():
    s = input()

    if len(s) < 3:
        if s == "8":
            print("Yes")
            return 0

        else:
            x = int(s) % 8
            y = int(s[::-1]) % 8
            if (x == 0) or (y == 0):
                print("Yes")
                return 0

    cnt = Counter(s)
    for i in range(112, 1000, 8):
        if not Counter(str(i)) - cnt:  
            print("Yes")
            return 0

    print("No")

main()