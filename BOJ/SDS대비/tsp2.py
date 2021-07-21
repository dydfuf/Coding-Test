import sys
from itertools import permutations

input = sys.stdin.readline


def calc(perm):
    result = 0
    for i in range(len(perm) - 1):
        if graph[perm[i] - 1][perm[i + 1] - 1] == 0:
            return -1
        result += graph[perm[i] - 1][perm[i + 1] - 1]

    return result


def goBack(perm, dest):
    result = 0
    for i in range(len(perm) - 1):
        if graph[perm[i]-1][dest-1] != 0:
            result += graph[perm[i]-1][dest-1]
            return result
        else:
            return -1


if __name__ == "__main__":
    N = int(input())
    graph = [[] for _ in range(N)]

    for i in range(N):
        graph[i] = list(map(int, input().split()))

    perm = permutations([i + 1 for i in range(N)])

    result = 9999999
    for aPerm in perm:
        aPerm = list(aPerm)

        reach = calc(aPerm)

        if not reach == -1:
            backPerm = aPerm[::-1]
            back = goBack(backPerm, aPerm[0])
            if not back == -1:
                reach = reach + back
                result = min(result, reach)

    print(result)