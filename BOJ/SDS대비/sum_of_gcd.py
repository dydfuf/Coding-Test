import sys

input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):

        data = list(map(int, input().split()))

        case = list()
        result = 0

        for i in range(data[0]):
            case.append(data[i + 1])

        for i in range(len(case)):
            for j in range(i + 1, len(case)):
                result += gcd(case[i], case[j])

        print(result)
