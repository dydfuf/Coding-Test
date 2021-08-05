def checkOne(string):
    result = 0
    for aS in string:
        if aS == "1":
            result += 1
    return result


def solution(n):
    oneCountOfN = checkOne(bin(n))
    temp = n + 1
    while True:
        if checkOne(bin(temp)) == oneCountOfN:
            return temp
        temp += 1


if __name__ == '__main__':
    arr_n = [78, 15]
    for n in arr_n:
        print(solution(n))
