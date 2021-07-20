import sys

input = sys.stdin.readline

if __name__ == "__main__":
    isPrime = [0] * 1000001

    isPrime[1] = 1
    for i in range(2, 1000001):
        if not isPrime[i]:
            temp = i + i
            while temp < 1000001:
                isPrime[temp] = 1
                temp += i

    primes = list()
    for i in range(1, len(isPrime)):
        if not isPrime[i]:
            primes.append(i)

    while True:
        n = int(input())
        if n == 0:
            break
        for prime in primes:
            if not isPrime[n-prime]:
                print(n, "=", prime, "+", n - prime)
                break
