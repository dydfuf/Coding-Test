import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())

    result = len(A)
    for aA in A:
        aA -= B
        if aA <= 0:
            continue
        if aA % C == 0:
            result += aA // C
        else:
            result += aA // C
            result += 1

    print(result)