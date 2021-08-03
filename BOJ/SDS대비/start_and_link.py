import sys
input = sys.stdin.readline
from itertools import combinations

if __name__ == "__main__":
    N = int(input())
    nums = [i for i in range(N)]
    table = list()
    for _ in range(N):
        s = list(map(int, input().split()))
        table.append(s)

    comb = list(combinations(nums, N//2))

    result = list()
    for aComb in comb:
        aComb = list(aComb)
        temp = list()
        for aNums in nums:
            if aNums not in aComb:
                temp.append(aNums)

        c_value = 0
        t_value = 0
        for i in aComb:
            for j in aComb:
                c_value += table[i][j]

        for i in temp:
            for j in temp:
                t_value += table[i][j]
        result.append(abs(c_value - t_value))

    print(min(result))


