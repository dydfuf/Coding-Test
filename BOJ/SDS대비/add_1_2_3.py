import sys
input = sys.stdin.readline

if __name__ == "__main__":
    """
    1 -> 1 [ 1 ]
    2 -> 2 [ 11, 2 ]
    3 -> 4 [ 1+2, 2+1, 3+0 ]
    4 -> 7 [ 1+3 2+2 3+1 ] -> [ 4 2 1 ] 7
    5 -> 13 [ 1+4 2+3 3+2 ] => [ 7 4 2 ] 13
    6 -> 24 [ 1+5
    7 -> 44 [ 331, 322
    8 -> 81
    9 -> 149
    10 -> 274
    """

    dp = [0] * 11
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, 11):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    T = int(input())
    for _ in range(T):
        n = int(input())
        print(dp[n])