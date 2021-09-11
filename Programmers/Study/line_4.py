from collections import deque


def solution(n):
    answer = []

    # 소수 구하기
    a = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False

    # 소인수 분해
    number = n
    fact = []
    for prime in primes:
        degree = 0
        while number % prime == 0:
            degree += 1
            number = number // prime
            fact.append(prime)
        if number == 1:
            break

    _list = deque([[i + 1 for i in range(n)]])
    for f in fact[:-1]:

        a = []
        while _list:
            _dict = dict()
            for i in range(f):
                _dict[i] = []
            temp = _list.popleft()

            for idx, item in enumerate(temp):
                rest = idx % f
                _dict[rest].append(item)

            for val in _dict.values():
                a.append(val)

        for aa in a:
            _list.append(aa)

    for a in _list:
        for c in a:
            answer.append(c)

    return answer


if __name__ == '__main__':
    arr_n = [12, 18]
    arr_result = [[1, 5, 9, 3, 7, 11, 2, 6, 10, 4, 8, 12],
                  [1, 7, 13, 3, 9, 15, 5, 11, 17, 2, 8, 14, 4, 10, 16, 6, 12, 18]]

    for n, result in zip(arr_n, arr_result):
        print(solution(n), result)
