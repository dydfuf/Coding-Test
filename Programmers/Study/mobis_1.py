from itertools import combinations, permutations

def solution(dice):
    answer = 0
    length = len(dice)

    all = sum(dice, [])

    for i in range(1, 10):
        if i not in all:
            return i

    for i in range(11, 100):
        ten = i // 10
        one = i % 10
        arrTen = []
        arrOne = []
        for j in range(length):
            if ten in dice[j]:
                arrTen.append(j)
            if one in dice[j]:
                arrOne.append(j)

        if len(arrTen) == 1 and len(arrOne) == 1 and arrTen == arrOne:
            return i

    for i in range(101, 1000):
        hund = i // 100
        ten = (i - hund*100) // 10
        one = (i - hund*100 - ten*10)

        arrHund = []
        arrTen = []
        arrOne = []

        for j in range(length):
            if hund in dice[j]:
                arrHund.append(j)
            if ten in dice[j]:
                arrTen.append(j)
            if one in dice[j]:
                arrOne.append(j)

        if len(arrHund) == 1 and len(arrTen) == 1 and len(arrOne) and arrHund == arrTen == arrOne:
            return i

    for i in range(1001, 10000):
        thous = i // 1000
        hund = (i - thous*1000) // 100
        ten = (i - thous*1000 - hund*100) // 10
        one = (i - thous*1000 - hund*100 - ten*10)

        arrThous = []
        arrHund = []
        arrTen = []
        arrOne = []

        for j in range(length):
            if thous in dice[j]:
                arrThous.append(j)
            if hund in dice[j]:
                arrHund.append(j)
            if ten in dice[j]:
                arrTen.append(j)
            if one in dice[j]:
                arrOne.append(j)

        if len(arrThous) == 1 and len(arrHund) == 1 and len(arrTen) == 1 and len(arrOne) and arrThous == arrHund == arrTen == arrOne:
            return i

    return answer

if __name__ == '__main__':
    arr_dice = [[[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]], [[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]]]
    arr_result = [22, 66]
    for dice, result in zip(arr_dice, arr_result):
        print(solution(dice), result)