import sys
from itertools import combinations

input = sys.stdin.readline

if __name__ == "__main__":
    N, S = map(int, input().split())

    data = list(map(int, input().split()))

    result = 0

    for i in range(1, N+1):
        comb = list(combinations(data,i))
        for aComb in comb:
            if sum(aComb) == S:
                result += 1

    print(result)
