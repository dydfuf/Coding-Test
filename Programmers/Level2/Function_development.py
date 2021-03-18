def solution(progresses, speeds):
    answer = []
    days = []
    for aProgress, aSpeeds in zip(progresses, speeds):
        remain = 100 - aProgress
        if remain % aSpeeds == 0:
            days.append(remain // aSpeeds)
        else:
            days.append((remain // aSpeeds) + 1)

    # 7 2 9
    temp = 0
    while len(days) > 0:
        temp = days.pop(0)
        cnt = 1
        temp_days = days.copy()
        for i in range(len(days)):
            if temp >= days[i]:
               cnt += 1
               temp_days.pop(0)
            else:
                break
        answer.append(cnt)
        days = temp_days.copy()
    return answer


if __name__ == "__main__":
    arr_progresses = [[93, 30, 55], [95, 90, 99, 99, 80, 99]]
    arr_speeds = [[1, 30, 5], [1, 1, 1, 1, 1, 1]]
    for progresses, speeds in zip(arr_progresses, arr_speeds):
        print(solution(progresses, speeds))

# 7 2 9
# 5 10 1 1 20 1 ,1 3 3