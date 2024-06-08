from collections import deque, defaultdict

def calc_longest_dist(m, f, n):
    deq = deque()
    deq.append([f, 0])
    p = 0
    d = 0
    visited = [0 for i in range(n)]
    while len(deq) != 0:
        p, d = deq.popleft()
        for i in m[p]:
            if visited[i] == 0:
                deq.append([i, d+1])
                visited[i] = 1
    return p, d

def main():
    n = int(input())
    m = defaultdict(list)
    for _ in range(n - 1):
        p1, p2 = map(int, input().split())
        m[p1-1].append(p2-1)
        m[p2-1].append(p1-1)
    pos, dist = calc_longest_dist(m, 0, n)
    _, dist = calc_longest_dist(m, pos, n)
    print(dist + 1)
    
if __name__ == "__main__":
    main()