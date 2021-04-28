import sys

sys.setrecursionlimit(300000)


def isAllZero(arr):
    for a in arr:
        if a != 0:
            return False
    else:
        return True


def solution2(a, edges):
    answer = 0

    # 0으로 만들 수 없으면 -1을 리턴
    if sum(a) != 0:
        return -1

    # 간선이 1개인것은 리프노드다
    leaf = []
    for i in range(len(a)):
        aA_edge = 0
        for edge in edges:
            if i in edge:
                aA_edge += 1
            if aA_edge > 1:
                break
        else:
            leaf.append([a[i], i])

    while not isAllZero(a):

        max_leaf = max(leaf)
        max_leaf_edge = 0
        for edge in edges:
            if max_leaf[1] == edge[0]:
                max_leaf_edge += edge[1]
            elif max_leaf[1] == edge[1]:
                max_leaf_edge += edge[0]

        a[max_leaf[1]] -= max_leaf[0]
        a[max_leaf_edge] += max_leaf[0]
        answer += max_leaf[0]

        # 부모가 자식이 더이상 없으면 leaf에 추가
        for edge in edges:
            if max_leaf[1] == edge[0]:
                # edge[1] <- 정점의 자식의 개수 확인해야함
                return
            elif max_leaf[1] == edge[1]:
                # edge[0] <- 정점의 자식의 개수 확인해야함
                return
            if max_leaf[1] in edge:
                edges.remove(edge)

    return answer

from collections import defaultdict
def dfs(idx, a, board):
    global visited
    global answer

    now = a[idx]
    visited[idx] = 1

    for i in board[idx]:
        if visited[i] == 0:
            now += dfs(i, a, board)

    answer += abs(now)

    return now

def solution(a, edges):
    global answer
    global visited
    answer = 0
    if sum(a) != 0:
        return -1
    board = [list() for _ in range(len(a))]
    visited = [0] * len(a)
    for i,j in edges:
        board[i].append(j)
        board[j].append(i)

    dfs(0, a, board)
    return answer


if __name__ == "__main__":
    arr_a = [
        [-5, 0, 2, 1, 2],
        [0, 1, 0],
        [-5000000000, 0, 2000000000, 1000000000, 2000000000],
    ]
    arr_edges = [
        [[0, 1], [3, 4], [2, 3], [0, 3]],
        [[0, 1], [1, 2]],
        [[0, 1], [3, 4], [2, 3], [0, 3]],
    ]
    for a, edges in zip(arr_a, arr_edges):
        print(solution(a, edges))
