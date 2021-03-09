def to_binary(n, digit):
    result = []
    while digit > 0:
        result.append(digit % 2)
        digit //= 2
    result = list(reversed(result))
    while len(result) < n:
        result.insert(0, 0)
    return result

def sum_list(l1, l2):
    result = []
    for i1, i2 in zip(l1, l2):
        result.append(i1 + i2)
    return result

def solution(n, arr1, arr2):
    answer = []
    bi_arr1 = []
    bi_arr2 = []

    for digit1, digit2 in zip(arr1, arr2):
        bi_arr1.append(to_binary(n, digit1))
        bi_arr2.append(to_binary(n, digit2))

    secret_map = []
    for l1, l2 in zip(bi_arr1, bi_arr2):
        secret_map.append(sum_list(l1, l2))

    for line in secret_map:
        result_line = ""
        for item in line:
            if item != 0:
                result_line += "#"
            elif item == 0:
                result_line += " "
        answer.append(result_line)
    return answer


if __name__ == "__main__":
    arr_n = [5, 6]
    arr_arr1 = [[9, 20, 28, 18, 11], [46, 33, 33 ,22, 31, 50]]
    arr_arr2 = [[30, 1, 21, 17, 28], [27 ,56, 19, 14, 14, 10]]
    for n, arr1, arr2 in zip(arr_n, arr_arr1, arr_arr2):
        print(solution(n, arr1, arr2))