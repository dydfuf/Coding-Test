import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    N, M, V = map(int, input().split())

    arr = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a-1].append(b-1)
        arr[b-1].append(a-1)

    for aArr in arr:
        aArr.sort()

    visited = [False] * N


    dfsArr = []
    def dfs(idx):
        dfsArr.append(idx+1)
        visited[idx] = True

        for dest in list(arr[idx]):
            if not visited[dest]:
                visited[dest] = True
                dfs(dest)

    bfsArr = []
    que = deque()
    def bfs(idx):
        visited[idx] = True
        que.append(idx)
        while len(que) > 0:
            idx = que.popleft()
            bfsArr.append(idx+1)
            for dest in list(arr[idx]):
                if not visited[dest]:
                    visited[dest] = True
                    que.append(dest)

    dfs(V-1)
    print(*dfsArr)
    visited = [False] * N
    bfs(V-1)
    print(*bfsArr)