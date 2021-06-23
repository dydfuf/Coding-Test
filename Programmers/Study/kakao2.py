def DFS(x, y, places, dist, x_count):
    global visited
    global isC
    visited[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    # print(x, y, dist)
    if dist == 2:
        isC = True
        return
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < 5 and 0 <= yy < 5:
            if visited[xx][yy] == 0:
                a = places[xx][yy]
                if places[xx][yy] == "O":
                    DFS(xx, yy, places, dist=dist + 1, x_count=x_count)
                elif places[xx][yy] == "X":
                    DFS(xx, yy, places, dist=dist+1, x_count=x_count+1)
                elif places[xx][yy] == "P":
                    if x_count == 0:
                        # print("P : ", xx, yy, dist, x_count)
                        isC = False
                    DFS(xx, yy, places, dist=dist+1, x_count=x_count)

    return

def solution(places):
    answer = []

    n = len(places)
    global visited
    global isC
    for aPlace in places:
        print(aPlace)
        visited = [[False] * n for _ in range(n)]
        isC = True
        for i in range(n):
            for j in range(n):
                if aPlace[i][j] == "P":
                    DFS(i, j, aPlace, dist=0, x_count=0)
        if isC:
            answer.append(1)
        else:
            answer.append(0)
    return answer


if __name__ == "__main__":
    print(solution([["PXOOP", "OPXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                    ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
