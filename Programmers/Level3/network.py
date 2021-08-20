def dfs(computers, parent, i):
    length = len(computers)
    for j in range(length):
        if computers[i][j] == 1 and not i == j and j == parent[j]:
            parent[j] = parent[i]
            dfs(computers, parent, j)


def solution(n, computers):
    parent = [i for i in range(n)]
    for i in range(n):
        dfs(computers, parent, i)

    answer = len(set(parent))

    return answer


if __name__ == '__main__':
    arr_n = [3, 3, 4]
    arr_computers = [[[1, 1, 0], [1, 1, 0], [0, 0, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
                     [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]]
    for n, computers in zip(arr_n, arr_computers):
        print(solution(n, computers))

