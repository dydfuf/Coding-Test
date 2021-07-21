import sys
from itertools import permutations

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    data = [i+1 for i in range(N)]

    per = list(permutations(data, N))

    for aPer in per:
        print(*aPer)