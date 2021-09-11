def dateToDay(date):
    y, m, d = date.split("-")

    return int(m) * 30 + int(d)


def solution(records, k, date):
    answer = []

    _dict = dict()

    _date = dateToDay(date)

    cri_date = _date - (k-1)

    for record in records:
        dateSp, userId, pId = record.split(" ")

        if pId in _dict.keys():
            _dict[pId].append((dateToDay(dateSp), userId))
        else:
            _dict[pId] = [(dateToDay(dateSp), userId)]

    reorder = dict()

    for key in _dict.keys():
        for item in _dict[key]:
            if cri_date <= item[0] <= _date:
                if key in reorder.keys():
                    reorder[key].append(item[1])
                else:
                    reorder[key] = [item[1]]

    temp = []
    for key in reorder.keys():
        _set = set(reorder[key])
        reorderCount = 0
        for aSet in _set:
            if reorder[key].count(aSet) > 1:
                reorderCount += 1
                continue
        temp.append([(reorderCount / len(_set)), len(reorder[key]), key[3:]])

    temp.sort(key = lambda x: (-x[0], -x[1], int(x[2])))

    if temp:
        for i in temp:
            answer.append("pid" + str(i[2]))
    else:
        return ['no result']

    return answer


if __name__ == '__main__':
    arr_records = [["2020-02-02 uid1 pid1", "2020-02-26 uid1 pid1", "2020-02-26 uid2 pid1", "2020-02-27 uid3 pid2",
                    "2020-02-28 uid4 pid2", "2020-02-29 uid3 pid3", "2020-03-01 uid4 pid3", "2020-03-03 uid1 pid1",
                    "2020-03-04 uid2 pid1", "2020-03-05 uid3 pid2", "2020-03-05 uid3 pid3", "2020-03-05 uid3 pid3",
                    "2020-03-06 uid1 pid4"],
                   ["2020-02-02 uid141 pid141", "2020-02-03 uid141 pid32", "2020-02-04 uid32 pid32",
                    "2020-02-05 uid32 pid141"],
                   ["2020-01-01 uid1000 pid5000"]]
    arr_k = [10, 10, 10]
    arr_date = ["2020-03-05", "2020-02-05", "2020-01-11"]
    arr_result = [["pid1", "pid3", "pid2"], ["pid32", "pid141"], ["no result"]]

    for records, k, date, result in zip(arr_records, arr_k, arr_date, arr_result):
        print(solution(records, k, date), result)
