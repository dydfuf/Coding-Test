import sys
from itertools import product
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    data = sorted(list(map(int, input().split())))

    perm = list(product(data, repeat=M))

    for aPerm in perm:
        print(*aPerm)
