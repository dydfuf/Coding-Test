def solution(n, m):
    answer = []
    gcd = 0
    for i in range(1, min(n,m) + 1):
        if n % i == 0 and m % i == 0:
            gcd = i

    answer.append(gcd)

    answer.append(int((n * m) / answer[0]))

    return answer


if __name__ == "__main__":
    n, m = 1, 1
    print(solution(n, m))
    n, m = 100, 99
    print(solution(n, m))
