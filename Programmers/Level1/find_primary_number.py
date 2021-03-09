def solution(n):
    answer = 0
    dp = [True] * (n + 1)

    for i in range(2, n + 1):
        if dp[i]:
            answer += 1
            dp[i] = False
            temp = i
            idx = 1
            while temp * idx <= n:
                dp[temp * idx] = False
                idx += 1

    return answer


def solution2(n):
    num = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)


if __name__ == "__main__":
    n = 10
    print(solution2(n))
    n = 5
    print(solution2(n))
