import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())

    table = list()

    for _ in range(N):
        table.append(list(map(int, input().split())))

    dp = [0] * N

    for i in range(N-1, -1, -1):
        T = table[i][0]
        P = table[i][1]

        if T > N - i:
            if i != N-1:
                dp[i] = dp[i+1]
            continue

        if i == N-1:
            dp[i] = P
        elif i + T == N:
            dp[i] = max(P, dp[i+1])
        else:
            dp[i] = max(P + dp[i + T], dp[i+1])

    print(dp[0])