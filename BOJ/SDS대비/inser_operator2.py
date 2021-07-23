import sys
from itertools import permutations

input = sys.stdin.readline


def calc(value, idx):
    global up, down
    if idx == (N-1):
        up = max(up, value)
        down = min(down, value)
        return

    for i in range(4):
        if oper[i] != 0:
            oper[i] -= 1
            if i == 0:
                calc(value+data[idx+1], idx+1)
            elif i == 1:
                calc(value-data[idx+1], idx+1)
            elif i == 2:
                calc(value*data[idx+1], idx+1)
            else:
                calc(int(value/data[idx+1]), idx+1)

            oper[i] += 1

if __name__ == "__main__":
    N = int(input())
    data = list(map(int, input().split()))
    oper = list(map(int, input().split()))

    up = -999999999
    down = 999999999

    calc(data[0], 0)
    print(up)
    print(down)