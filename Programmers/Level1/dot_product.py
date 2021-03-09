def solution(a, b):
    answer = 0

    for i in range(0, len(a)):
        answer += a[i] * b[i]

    return answer


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    b = [-3, -1, 0, 2]
    print(solution(a, b))
    a = [-1, 0, 1]
    b = [1, 0, -1]
    print(solution(a, b))
