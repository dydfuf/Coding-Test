def solution(n):
    dp = [0] * (n+1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] % 1234567


if __name__ == '__main__':
    arr_n = [3, 5]
    for n in arr_n:
        print(solution(n))
