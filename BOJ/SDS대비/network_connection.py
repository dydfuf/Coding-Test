import sys

input = sys.stdin.readline


def find(table, target):
    if table[target] == target:
        return target

    return find(table, table[target])


def change(table, old, new):
    for i in range(len(table)):
        if table[i] == old:
            table[i] = new

    return table


if __name__ == "__main__":
    N = int(input())
    M = int(input())

    lines = list()
    cycle_table = [i for i in range(N + 1)]

    result = 0

    for _ in range(M):
        a, b, c = map(int, input().split())
        lines.append([c, a, b])

    lines.sort()

    for line in lines:
        b = find(cycle_table, line[1])
        c = find(cycle_table, line[2])
        if b != c:
            result += line[0]
            newParent = min(b,c)
            cycle_table = change(cycle_table, b, newParent)
            cycle_table = change(cycle_table, c, newParent)

    print(result)
