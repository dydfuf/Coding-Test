import sys
input = sys.stdin.readline

tree = list()
nodes = list()

def init(start, end, index):
    if start == end:
        tree[index] = nodes[start]
        return tree[index]
    mid = (start+end) // 2
    tree[index] = init(start, mid, index*2)+init(mid+1, end, index*2 + 1)
    return tree[index]

def update(start, end, index, changeIdx, changeNum):
    if changeIdx < start or changeIdx > end:
        return
    tree[index] += changeNum-nodes[changeIdx]
    if start == end:
        return
    mid = (start+end) // 2
    update(start, mid, index*2, changeIdx, changeNum)
    update(mid+1, end, index*2 + 1, changeIdx, changeNum)

def query(start, end, index, left, right):
    if left > end or right < start:
        return 0
    if start >= left and end <= right:
        return tree[index]
    mid = (start+end) // 2
    return query(start, mid, index*2, left, right) + query(mid+1, end, index*2+1, left, right)

if __name__ == "__main__":
    N, M, K = map(int, input().rstrip().split())
    for _ in range(N):
        nodes.append(int(input()))
    tree = [0] * (N * 4)
    init(0, N-1, 1)
    for _ in range(M+K):
        a, b, c = map(int, input().rstrip().split())
        if a == 1:
            update(0, N-1, 1, b-1, c)
            nodes[b-1] = c
        else:
            print(query(0, N-1, 1, b-1, c-1))