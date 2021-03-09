def solution(n):
    answer = 0
    dp = [True] * (n+1)

    for i in range(2, n+1):
        if dp[i]:
            answer += 1
            dp[i] = False
            temp = i
            idx = 1
            while temp*idx <= n:

                dp[temp*idx] = False
                idx += 1

    return answer


if __name__ == "__main__":
    n = 10
    print(solution(n))
    n = 5
    print(solution(n))