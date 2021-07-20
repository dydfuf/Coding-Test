import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
row, col = 0, 0
result = 0


def dfs(graph, x, y, count, sum):
    global result
    global visited

    if count >= 4:
        result = max(result, sum)
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(graph, nx, ny, count + 1, sum + graph[nx][ny])
            visited[nx][ny] = 0


def exception(graph, x, y):
    global result

    if 0 <= x + 2 < row and 0 <= y + 1 < col:
        value = graph[x][y] + graph[x + 1][y] + graph[x + 2][y] + graph[x + 1][y + 1]
        result = max(result, value)

    if 0 <= x + 1 < row and 0 <= y + 2 < col:
        value = graph[x][y] + graph[x][y + 1] + graph[x][y + 2] + graph[x + 1][y + 1]
        result = max(result, value)

    if 0 <= x - 1 and x + 1 < row and 0 <= y+1 < col:
        value = graph[x][y] + graph[x - 1][y + 1] + graph[x][y + 1] + graph[x + 1][y + 1]
        result = max(result, value)

    if 0 <= x - 1 and 0 <= y+2 < col:
        value = graph[x][y] + graph[x][y + 1] + graph[x][y + 2] + graph[x - 1][y + 1]
        result = max(result, value)


if __name__ == "__main__":
    row, col = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(row)]

    visited = [[0] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            visited[i][j] = 1
            dfs(graph, i, j, 1, graph[i][j])
            visited[i][j] = 0
            exception(graph, i, j)

    print(result)
