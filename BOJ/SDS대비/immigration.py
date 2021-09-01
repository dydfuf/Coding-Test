import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    data = list()
    for _ in range(N):
        data.append(int(input()))

    start = 0
    end = max(data) * M

    answer = end
    while start <= end:
        mid = (start + end) // 2

        temp = 0
        for i in data:
            temp += mid // i

        if temp < M:
            start = mid + 1
        else:
            answer = min(answer,mid)
            end = mid - 1

    print(answer)
