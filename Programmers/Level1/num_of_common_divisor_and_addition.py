def findCountOfDivisor(number):
    result = 0
    for i in range(1, number + 1):
        if number % i == 0:
            result += 1

    return result


def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        count = findCountOfDivisor(i)
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer


if __name__ == "__main__":
    arr_left = [13, 24]
    arr_right = [17, 27]
    for left, right in zip(arr_left, arr_right):
        print(solution(left, right))
