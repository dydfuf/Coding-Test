from itertools import combinations_with_replacement


def calc(info, temp):
    r = 0
    a = 0

    for i in range(11):
        ap = info[i]
        ri = temp[i]
        if ap == 0 and ri == 0:
            continue
        if ap >= ri:
            a += 10 - i
        else:
            r += 10 - i

    return r, a


def solution(n, info):

    temp = [i for i in range(11)]

    ans = [([], -1)]
    for comb in combinations_with_replacement(temp, n):
        lion = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for c in comb:
            lion[c] += 1
        r, a = calc(info, lion)

        # r이 이기는 경우
        if r > a:
            diff = r - a
            if diff > ans[0][1]:
                ans = [(lion, diff)]
            elif diff == ans[0][1]:
                ans.append((lion, diff))

    if ans[0][1] == -1:
        return [-1]
    elif len(ans) == 1:
        return ans[0][0]
    else:
        maxIdx = 0
        for a in ans:
            for idx, aa in enumerate(a[0]):
                if aa != 0 and idx > maxIdx:
                    maxIdx = idx

        res = [[], 0]
        for a in ans:
            if a[0][maxIdx] != 0 and a[0][maxIdx] > res[1]:
                res = [a[0], a[0][maxIdx]]
        return res[0]


if __name__ == '__main__':
    arr_n = [5, 1, 9, 10, 5]
    arr_info = [[2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3], [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]]
    arr_result = [[0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0], [-1], [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0],
                  [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for n, info, result in zip(arr_n, arr_info, arr_result):
        print(solution(n, info), result)

    print(solution(2, [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]))
