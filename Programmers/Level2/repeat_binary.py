def removeZero(string):
    result = string.count("0")
    newString = string.replace("0", "")

    return newString, result


def lengthToBinary(string):
    result = ""

    length = len(string)

    while length > 0:
        result += str(length % 2)
        length //= 2

    return result[::-1]


def solution(s):
    answer = [0, 0]

    while s != "1":
        # 0을 제거
        s, count = removeZero(s)
        # length to binary
        s = lengthToBinary(s)

        answer[0] += 1
        answer[1] += count

    return answer


if __name__ == '__main__':
    arr_s = ["110010101001", "01110", "1111111"]
    arr_result = [[3, 8], [3, 3], [4, 1]]
    for s, result in zip(arr_s, arr_result):
        print(solution(s), result)
