import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().split())
    data = []

    for _ in range(N):
        data.append(int(input()))

    start = max(data)
    end = 0

    answer = 0
    while True:
        mid = (start + end) // 2
        if mid == 0:
            answer = 1
            break
        if start < end:
            answer = start
            break
        temp = 0
        for i in data:
            temp += i // mid

        if temp >= K:
            end = mid + 1
        else:
            start = mid - 1

    print(answer)
