def solution(n):
    answer = []

    n = str(n)
    n = n[::-1]

    for c in n:
        answer.append(int(c))

    return answer


if __name__ == "__main__":
    n = 12345
    print(solution(n))