def solution(numbers):
    return 45 - sum(numbers)

if __name__ == '__main__':
    arr_numbers = [[1,2,3,4,6,7,8,0]	, [5,8,4,0,6,7,9]	]
    arr_result = [14, 6]

    for numbers, result in zip(arr_numbers, arr_result):
        print(solution(numbers), result)