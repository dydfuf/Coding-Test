import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, S = map(int, input().split())
    data = list(map(int, input().split()))

    start = 0
    end = 1
    result = 1000001

    sums = [0] * (N + 1)
    for i in range(1, N + 1):
        sums[i] = sums[i - 1] + data[i - 1]

    while start != N:
        if sums[end] - sums[start] >= S:
            if end - start < result:
                result = end - start
            start += 1
        else:
            if end != N:
                end += 1
            else:
                start += 1

    if result != 1000001:
        print(result)
    else:
        print(0)
