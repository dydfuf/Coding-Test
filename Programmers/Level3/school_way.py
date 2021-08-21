def solution(m, n, puddles):
    ways = [[1 for _ in range(m)] for _ in range(n)]

    for puddle in puddles:
        ways[puddle[1] - 1][puddle[0] - 1] = 0

    for i in range(m):
        if ways[0][i] == 0:
            for j in range(i, m):
                ways[0][j] = 0

    for i in range(n):
        if ways[i][0] == 0:
            for j in range(i, n):
                ways[j][0] = 0

    for i in range(1, n):
        for j in range(1, m):
            if not ways[i][j] == 0:
                ways[i][j] = ways[i - 1][j] + ways[i][j - 1]

    return ways[-1][-1] % 1000000007


if __name__ == '__main__':
    print(solution(2, 2, []), 2)
    print(solution(3, 3, []), 6)
    print(solution(3, 3, [[2, 2]]), 2)
    print(solution(3, 3, [[2, 3]]), 3)
    print(solution(3, 3, [[1, 3]]), 5)
    print(solution(3, 3, [[1, 3], [3, 1]]), 4)
    print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
    print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
    print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0)
    print(solution(4, 4, [[3, 2], [2, 4]]), 7)
    print(solution(100, 100, []), 690285631)