import sys

input = sys.stdin.readline


def gcd(a, b):
    result = 1
    small = min(a, b)
    for i in range(1, small + 1):
        if a % i == 0 and b % i == 0:
            result = i

    return result


if __name__ == "__main__":
    M, N = map(int, input().split())

    g = gcd(M, N)
    l = int(M * N / g)
    print(g)
    print(l)
