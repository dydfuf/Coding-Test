def gcd(a, b):
    while (b != 0):
        temp = a % b
        a = b
        b = temp
    return abs(a)


def lcm(a, b):
    gcd_value = gcd(a, b)
    if (gcd_value == 0): return 0
    return abs((a * b) / gcd_value)


def solution(arr):

    answer = lcm(arr[0], arr[1])
    for i in range(2, len(arr)):
        answer = lcm(answer, arr[i])
    return int(answer)


if __name__ == '__main__':
    arr_arr = [[2, 6, 8, 14], [1, 2, 3]]

    for arr in arr_arr:
        print(solution(arr))
