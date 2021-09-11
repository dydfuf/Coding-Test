def solution(id_list, report, k):
    answer = []

    report = set(report)
    report = list(report)
    dictReport = dict()
    reported = dict()


    for id in id_list:
        dictReport[id] = set()
        reported[id] = 0

    for aReport in report:
        user, userReport = aReport.split(" ")
        dictReport[user].add(userReport)
        reported[userReport] += 1

    for key in dictReport.keys():
        temp = 0
        for item in dictReport[key]:
            if reported[item] >= k:
                temp += 1
        answer.append(temp)

    return answer


if __name__ == '__main__':
    arr_id_list = [["muzi", "frodo", "apeach", "neo"], ["con", "ryan"]]
    arr_report = [["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
                  ["ryan con", "ryan con", "ryan con", "ryan con"]]
    arr_k = [2, 3]
    arr_result = [[2, 1, 1, 0], [0, 0]]

    for id_list, report, k, result in zip(arr_id_list, arr_report, arr_k, arr_result):
        print(solution(id_list, report, k), result)