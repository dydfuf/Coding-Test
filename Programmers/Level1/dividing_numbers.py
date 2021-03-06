def solution(arr, divisor):
    answer = []

    for a in arr:
        if a % divisor == 0:
            answer.append(a)

    answer.sort()

    if len(answer) == 0:
        answer.append(-1)
    return answer


if __name__ == "__main__":
    arr = [5, 9, 7, 10]
    divisor = 5
    print(solution(arr, divisor))