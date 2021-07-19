import sys

input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
sys.setrecursionlimit(100000)

def find(target):
    if target == parent[target]:
        return target

    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    flag, a, b = map(int, input().split())
    if flag:
        if find(a) == find(b):
            print('yes')
        else:
            print('no')
    else:
        union(a, b)
