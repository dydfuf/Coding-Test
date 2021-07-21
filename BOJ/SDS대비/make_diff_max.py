import sys
from itertools import permutations

input = sys.stdin.readline


def calc(a):
    result = 0
    for i in range(2, len(a) + 1):
        result += abs(a[i - 2] - a[i - 1])
    return result


if __name__ == "__main__":
    N = int(input())
    data = list(map(int, input().split()))

    permutations = permutations(data, N)

    result = 0
    for aPermutation in permutations:
        temp = calc(list(aPermutation))
        if temp > result:
            result = temp

    print(result)

