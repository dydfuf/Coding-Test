import sys
from itertools import permutations

input = sys.stdin.readline

if __name__ == "__main__":
    dwarfs = list()
    sum_of_dwarfs = 0
    for _ in range(9):
        temp = int(input())
        dwarfs.append(temp)
        sum_of_dwarfs += temp

    permutations_of_dwarfs = list(permutations(dwarfs, 2))
    diff = sum_of_dwarfs - 100
    for aPermutation in permutations_of_dwarfs:
        if sum(aPermutation) == diff:
            dwarfs.pop(dwarfs.index(int(aPermutation[0])))
            dwarfs.pop(dwarfs.index(int(aPermutation[1])))
            break
    dwarfs.sort()
    for dwarf in dwarfs:
        print(dwarf)

