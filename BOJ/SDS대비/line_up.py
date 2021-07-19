import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    inDegree = [0 for _ in range(n + 1)]

    q = deque()
    result = []

    for _ in range(m):
        f, b = map(int, input().split())
        graph[f].append(b)
        inDegree[b] += 1

    for i in range(1, n+1):
        if inDegree[i] == 0:
            q.append(i)

    while q:
        a = q.popleft()
        result.append(a)
        for g in graph[a]:
            inDegree[g] -= 1
            if inDegree[g] == 0:
                q.append(g)
    print(*result)
