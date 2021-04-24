def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = ''.join(numbers)

    return answer


if __name__ == "__main__":
    arr_numbers = [[6, 10, 2], [3, 30, 34, 5, 9]]
    for numbers in arr_numbers:
        print(solution(numbers))
