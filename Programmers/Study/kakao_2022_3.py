from math import ceil


def timeToMin(timeStr):
    result = 0

    minute, second = timeStr.split(":")

    result += int(minute) * 60 + int(second)

    return result


def calFee(fees, time):
    basicTime, basicFee, unitTime, unitFee = fees
    fee = basicFee

    if time <= basicTime:
        return fee
    else:
        time = time - basicTime
        fee += ceil(time / unitTime) * unitFee

    return fee


def solution(fees, records):
    answer = []

    _dict = dict()

    for record in records:
        time, carNum, IN_OUT = record.split(" ")

        if carNum in _dict.keys():
            _dict[carNum].append(time)
        else:
            _dict[carNum] = [time]

    _time = dict()
    for key in _dict.keys():
        if len(_dict[key]) % 2 == 1:
            _dict[key].append("23:59")

        _time[key] = 0
        temp = _dict[key][:]

        while temp:
            a = timeToMin(temp[0])
            b = timeToMin(temp[1])
            _time[key] += b - a
            temp.pop(0)
            temp.pop(0)

    ans = []
    for key in _time.keys():
        ans.append([key, calFee(fees, _time[key])])

    ans.sort(key=lambda x: x[0])

    for aAns in ans:
        answer.append(aAns[1])

    return answer


if __name__ == '__main__':
    arr_fees = [[180, 5000, 10, 600], [120, 0, 60, 591], [1, 461, 1, 10]]
    arr_records = [
        ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
         "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"],
        ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"],
        ["00:00 1234 IN"]]
    arr_result = [[14600, 34400, 5000], [0, 591], [14841]]

    for fees, records, result in zip(arr_fees, arr_records, arr_result):
        print(solution(fees, records), result)
