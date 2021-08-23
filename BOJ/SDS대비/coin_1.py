import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = []
    for i in range(n):
        coins.append(int(input()))

    count_list = [0] * (k + 1)
    count_list[0] = 1

    for coin in coins:
        for i in range(coin, k + 1):
            count_list[i] += count_list[i - coin]

    print(count_list)