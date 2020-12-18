s = input()
k = int(input())

st = set()
if len(s) < k:
    print("0")
else:
    for i in range(0, len(s)-k+1):
        if s[i:i+k] not in st:
            st.add(s[i:i+k])
    print(len(st))