def solution(n):
    answer = 0
    ternary = ''
    while n > 0:
        ternary = ternary + str(n % 3)
        n //= 3

    temp = 1
    for i in range(len(ternary)-1, -1, -1):
        answer += int(ternary[i]) * temp
        temp *= 3

    return answer


if __name__ == "__main__":
    n = 45
    print(solution(n))