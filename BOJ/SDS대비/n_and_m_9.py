import sys
from itertools import combinations
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    data = sorted(list(map(int, input().split())))

    perm = sorted(list(set(combinations(data, M))))

    for aPerm in perm:
        print(*aPerm)
