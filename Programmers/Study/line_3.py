from collections import deque


def solution(jobs):
    answer = []

    jobs.sort(key=lambda x: x[0])

    notFinished = jobs[1:]
    wait = []

    time = jobs[0][0] + jobs[0][1]
    last = jobs[0][2]
    answer.append(jobs[0][2])
    while True:
        if not notFinished:
            break

        while True:
            if not notFinished:
                break
            if notFinished[0][0] >= time:
                break
            wait.append(notFinished.pop(0))

        _dict = dict()
        for aWait in wait:
            if aWait[2] in _dict.keys():
                _dict[aWait[2]] += aWait[3]
            else:
                _dict[aWait[2]] = aWait[3]

        temp = []
        for key in _dict.keys():
            temp.append([_dict[key], key])

        temp.sort(key=lambda x: (-x[0], x[1]))

        print("temp : ", temp)
        print("wait : ", wait)
        print("last : ", last)
        isLast = False
        for idx, aWait in enumerate(wait):
            idxes = []
            if aWait[2] == last:
                isLast = True
                idxes.append(idx)
                time += aWait[1]

            idxes.sort(reverse=True)
            for i in idxes:
                wait.pop(i)
        if isLast:
            print(time)
            continue

        if temp:
            next = temp[0][1]
        else:
            break
        for idx, aWait in enumerate(wait):
            idxes = []
            if aWait[2] == next:
                last = next
                time += aWait[1]
                idxes.append(idx)

            idxes.sort(reverse=True)
            for i in idxes:
                wait.pop(i)
        answer.append(next)

        print("time -> ", time)
    return answer


if __name__ == '__main__':
    arr_jobs = [[[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]],
                [[1, 2, 1, 5], [2, 1, 2, 100], [3, 2, 1, 5], [5, 2, 1, 5]],
                [[0, 2, 3, 1], [5, 3, 3, 1], [10, 2, 4, 1]],
                [[0, 5, 1, 1], [2, 4, 3, 3], [3, 4, 4, 5], [5, 2, 3, 2]]]
    arr_result = [[2, 1, 2, 3], [1, 2], [3, 4], [1, 3, 4]]

    for jobs, result in zip(arr_jobs, arr_result):
        print(solution(jobs), result)
