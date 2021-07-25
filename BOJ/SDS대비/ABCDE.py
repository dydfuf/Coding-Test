import sys

input = sys.stdin.readline


def dfs(graph, visited, idx, count):
    if count > 3:
        print(1)
        exit()

    for friend in graph[idx]:
        if not visited[friend]:
            visited[friend] = True
            dfs(graph, visited, friend, count + 1)
            visited[friend] = False


if __name__ == "__main__":
    N, M = map(int, input().split())

    graph = [[] for _ in range(N)]
    visited = [False] * N

    for _ in range(M):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)

    for i in range(N):
        visited[i] = True
        dfs(graph, visited, i, 0)
        visited[i] = False

    print(0)
