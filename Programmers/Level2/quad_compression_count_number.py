def split(input_arr):
    half = len(input_arr) // 2

    temp = []
    result = []
    for iidx in range(2):
        for idx in range(2):
            for i in range(half * iidx, half * (iidx + 1)):
                for j in range(half * idx, half * (idx + 1)):
                    temp.append(arr[i][j])
            cl_t = temp.copy()
            result.append(cl_t)
            temp.clear()

    if half == 1:
        return input_arr

    return result


def check(check_arr):
    checkNum = check_arr[0]
    for item in check_arr:
        if item != checkNum:
            return False
    return True


def solution(arr):
    answer = []
    zero_cnt = 0
    one_cnt = 0
    for row in arr:
        for item in row:
            if item == 0:
                zero_cnt += 1
            else:
                one_cnt += 1

    # half = len(arr) // 2
    # for iidx in range(2):
    #     for idx in range(2):
    #         for i in range(half*iidx, half*(iidx+1)):
    #             for j in range(half*idx, half*(idx+1)):
    #                 print(arr[i][j], end="")
    #         print()

    splited = split(arr)
    for aSplited in splited:
        if check(aSplited):
            if aSplited[0] == 0:
                zero_cnt -= len(aSplited) - 1
            else:
                one_cnt -= len(aSplited) - 1
        else:
            NewSplit = split(aSplited)
            print(NewSplit)

    return [zero_cnt, one_cnt]


if __name__ == "__main__":
    arr_arr = [[[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]],
               [[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]]
    for arr in arr_arr:
        print(solution(arr))
