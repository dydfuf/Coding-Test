import sys
from itertools import permutations
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    data = sorted(list(map(int, input().split())))

    perm = list(permutations(data, M))

    for aPerm in perm:
        print(*aPerm)
