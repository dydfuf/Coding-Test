import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, C = map(int, input().split())
    data = [int(input()) for _ in range(N)]

    data.sort()

    start = 1
    end = data[-1] - data[0]

    result = 0

    while start <= end:
        mid = (start + end) // 2
        value = data[0]
        count = 1

        for i in range(1, len(data)):
            if data[i] >= value + mid:
                value = data[i]
                count += 1

        if count >= C:
            start = mid + 1
            result = mid
        else:
            end = mid - 1

    print(result)