import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    data = [i + 1 for i in range(N)]
    target = list(map(int, input().split()))

    find = False
    for i in range(N-1, 0, -1):
        if target[i] > target[i-1]:
            for j in range(N-1, 0, -1):
                if target[j] > target[i-1]:
                    target[i-1], target[j] = target[j], target[i-1]
                    target = target[:i] + sorted(target[i:])
                    find = True
                    break
        if find:
            print(*target)
            break
    if not find:
        print(-1)