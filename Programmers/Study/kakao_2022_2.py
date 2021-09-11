from itertools import combinations


def nTok(n, k):
    result = ""

    while n > 0:
        result += str(n % k)
        n //= k

    return result[::-1]


def isPrimeDec(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 is 0 or n % 3 is 0:
        return False
    if n < 9:
        return True
    k, l = 5, n ** 0.5
    while k <= l:
        if n % k is 0 or n % (k + 2) is 0:
            return False
        k += 6
    return True


def isPrime(num):
    # case 1
    if num[0] == "0" and num[-1] == "0":
        nStr = num[1:-1]
    # case 2
    elif num[0] != "0" and num[-1] == "0":
        nStr = num[:-1]
    # case 3
    elif num[0] == "0" and num[-1] != "0":
        nStr = num[1:]
    # case 4
    else:
        nStr = num

    if not nStr:
        return [False, nStr]

    zeroCount = nStr.count("0")

    if zeroCount == 0 and isPrimeDec(int(nStr)):
        return [True, nStr]

    return [False, nStr]


def solution(n, k):
    answer = 0

    _nTok = nTok(n, k)

    cand = [_nTok]
    zeroIdx = []

    for idx, c in enumerate(_nTok):
        if c == "0":
            zeroIdx.append(idx)

    for zero in zeroIdx:
        cand.append(_nTok[:zero + 1])
        cand.append(_nTok[zero:])

    temp = [i for i in range(len(zeroIdx))]
    for comb in combinations(temp, 2):
        cand.append(_nTok[zeroIdx[comb[0]]: zeroIdx[comb[1]] + 1])

    for aCand in cand:
        isP, ns = isPrime(aCand)
        if isP:
            answer += 1

    return answer


# 11, 12, 14, 15, 16


if __name__ == '__main__':
    arr_n = [437674, 110011, 10, 1]
    arr_k = [3, 10, 10, 3]
    arr_result = [3, 2, 1, 1]

    for n, k, result in zip(arr_n, arr_k, arr_result):
        print(solution(n, k), result)
