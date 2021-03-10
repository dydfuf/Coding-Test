def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        if n % 3 == 0:
            answer += "1"
        elif n % 3 == 1:
            answer += "2"
        elif n % 3 == 2:
            answer += "4"
        n //= 3
    return answer[::-1]


if __name__ == "__main__":
    arr_n = [1, 2, 3, 4]
    for n in arr_n:
        print(solution(n))


# 10 41
# 11 42
# 12 44
# 13 111