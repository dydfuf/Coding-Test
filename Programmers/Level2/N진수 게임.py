def deciToNary(number, n):
    if number == 0:
        return "0"
    result = ""
    while number > 0:

        rest = number % n
        if rest == 10:
            result += 'A'
        elif rest == 11:
            result += 'B'
        elif rest == 12:
            result += 'C'
        elif rest == 13:
            result += 'D'
        elif rest == 14:
            result += 'E'
        elif rest == 15:
            result += 'F'
        else:
            result += str(rest)

        number //= n

    return result[::-1]


def solution(n, t, m, p):
    answer = ''
    gameStr = ''
    for i in range(m * t):
        gameStr += deciToNary(i, n)

    for i in range(p - 1, m * t, m):
        answer += gameStr[i]
    return answer


if __name__ == '__main__':
    arr_n = [2, 16, 16]
    arr_t = [4, 16, 16]
    arr_m = [2, 2, 2]
    arr_p = [1, 1, 2]
    for n, t, m, p in zip(arr_n, arr_t, arr_m, arr_p):
        print(solution(n, t, m, p))
