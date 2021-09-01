import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())

    data = list(map(int, input().split()))

    M = int(input())

    start = 1
    end = max(data)

    answer = 1
    while True:
        mid = (start + end) // 2

        if start > end:
            answer = mid
            break

        temp = 0
        for i in data:
            if mid < i:
                temp += mid
            else:
                temp += i
        if temp <= M:
            start = mid + 1
        else:
            end = mid - 1
    print(answer)