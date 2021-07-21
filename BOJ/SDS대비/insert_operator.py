import sys
from itertools import permutations

input = sys.stdin.readline


def calc(data, operators):
    # 123456
    # ++-*/
    mid = data[0]
    for idx, operator in enumerate(operators):
        if operator == "+":
            mid += data[idx + 1]
        elif operator == "-":
            mid -= data[idx + 1]
        elif operator == "*":
            mid *= data[idx + 1]
        elif operator == "/":
            if mid//data[idx + 1] < 0:
                mid = -(-mid//data[idx + 1])
            else:
                mid //= data[idx + 1]
    return mid


if __name__ == "__main__":
    N = int(input())
    data = list(map(int, input().split()))
    oper = list(map(int, input().split()))

    oper_str = ""
    for i in range(4):
        if i == 0:
            oper_str += "+" * oper[i]
        elif i == 1:
            oper_str += "-" * oper[i]
        elif i == 2:
            oper_str += "*" * oper[i]
        elif i == 3:
            oper_str += "/" * oper[i]
    oper_list = list(oper_str)

    perm = list(set(permutations(oper_list)))
    up = -999999999
    down = 999999999
    for aPerm in perm:
        result = calc(data, list(aPerm))
        if result > up:
            up = result
        if result < down:
            down = result
    print(up)
    print(down)