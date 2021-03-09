def solution(num):
    answer = 0
    while num != 1:
        if answer == 500:
            return -1
        if num % 2 == 0:
            num /= 2
        elif num % 2 == 1:
            num = num*3 + 1
        answer += 1
    return answer


if __name__ == "__main__":
    n = 6
    print(solution(n))
    n = 16
    print(solution(n))
    n = 626331
    print(solution(n))