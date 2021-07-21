import sys
from itertools import combinations
input = sys.stdin.readline

if __name__ == "__main__":
    while True:
        data = list(map(int, input().split()))
        if data[0] == 0:
            break

        numbers = data[1:]

        comb = combinations(numbers, 6)
        for aComb in comb:
            print(*aComb)
        print()