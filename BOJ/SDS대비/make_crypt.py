import sys
from itertools import combinations

input = sys.stdin.readline

if __name__ == "__main__":
    L, C = map(int, input().split())
    alpha = sorted(list(map(str, input().split())))

    comb = list(combinations(alpha, L))

    mo = ["a", "e", "i", "o", "u"]

    for aComb in comb:
        mo_count = 0
        for alpha in aComb:
            if alpha in mo:
                mo_count += 1
        if 0 < mo_count <= L - 2:
            print("".join(aComb))
