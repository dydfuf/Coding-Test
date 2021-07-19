N, M = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)
result = 0


def cutTree(H, trees):
    result = 0
    for tree in trees:
        if tree - H > 0:
            result += tree - H

    return result


while start <= end:
    mid = (start + end) // 2

    temp = cutTree(mid, data)

    if temp >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
