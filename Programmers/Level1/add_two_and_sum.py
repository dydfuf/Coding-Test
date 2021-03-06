def solution(numbers):
    answer = []
    answer = set(answer)

    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if i != j:
                answer.add(numbers[i] + numbers[j])

    answer = list(answer)
    answer.sort()
    return answer


if __name__ == "__main__":
    numbers = [2, 1, 3, 4, 1]
    print(solution(numbers))
    numbers = [5, 0, 2, 7]
    print(solution(numbers))
