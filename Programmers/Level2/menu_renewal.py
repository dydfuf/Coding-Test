from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        menus = dict()
        temps = list()

        for order in orders:
            for aComb in list(combinations(sorted(order), c)):
                temps.append(aComb)

        for temp in temps:

            key = "".join(temp)

            if key in menus:
                menus[key] += 1
            else:
                menus[key] = 1

        for menu in menus:
            if max(menus.values()) > 1:
                if menus[menu] == max(menus.values()):
                    answer.append(menu)

    answer.sort()

    return answer


if __name__ == '__main__':
    arr_orders = [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], ["XYZ", "XWY", "WXA"]]
    arr_course = [[2,3,4], [2,3,5], [2,3,4]	]
    arr_result = [["AC", "ACDE", "BCFG", "CDE"], ["ACD", "AD", "ADE", "CD", "XYZ"], ["WX", "XY"]]

    for orders, course, result in zip(arr_orders, arr_course, arr_result):
        print(solution(orders, course), result)