import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    data = sorted(list(map(int, input().split())))

    perm = list(combinations_with_replacement(data, M))

    for aPerm in perm:
        print(*aPerm)
