import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (N + 1)
    result = 0


    def dfs(idx):
        visited[idx] = True
        for i in graph[idx]:
            if not visited[i]:
                dfs(i)


    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            result += 1

    print(result)
