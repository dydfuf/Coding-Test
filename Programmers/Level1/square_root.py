def solution(n):
    idx = 1
    while True:
        if idx ** 2 == n:
            return (idx+1) ** 2
        else:
            idx += 1

        if idx ** 2 > n:
            return -1


if __name__ == "__main__":
    n = 121
    print(solution(n))
    n = 3
    print(solution(n))