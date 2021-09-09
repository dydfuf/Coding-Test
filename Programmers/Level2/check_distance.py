dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(table, x, y, count, visited, valid):
    if table[x][y] == "P" and count != 0 and count < 3:
        valid[0] = False
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and not table[nx][ny] == "X":
            visited[nx][ny] = True
            dfs(table, nx, ny, count + 1, visited, valid)
            visited[nx][ny] = False


def solution(places):
    answer = []
    for aPlace in places:
        visited = [[False for _ in range(5)] for _ in range(5)]
        valid = [True]
        for i in range(5):
            for j in range(5):
                if aPlace[i][j] == "P":
                    visited[i][j] = True
                    dfs(aPlace, i, j, 0, visited, valid)
                    visited[i][j] = False
        if valid[0]:
            answer.append(1)
        else:
            answer.append(0)
    return answer


if __name__ == '__main__':
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
              ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
              ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    result = [1, 0, 1, 1, 1]
    print(solution(places), result)
