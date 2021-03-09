def solution(n):
    answer = 0

    n = str(n)

    for c in n:
        answer += int(c)

    return answer


if __name__ == "__main__":
    N = 123
    print(solution(N))
    N = 987
    print(solution(N))