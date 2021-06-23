def up(current, count, table):
    upCount = 0
    temp = 1
    # if not table[current]:
    #     upCount += 1
    #     temp += 1
    while True:
        if upCount == count:
            current -= temp - 1
            break
        if table[current - temp]:
            upCount += 1
        temp += 1

    return current


def down(current, count, table):
    downCount = 0
    temp = 1
    # if not table[current]:
    #     downCount += 1
    #     temp += 1
    while True:
        if downCount == count:
            current += temp - 1
            break
        if table[current + temp]:
            downCount += 1
        temp += 1

    return current


def isEnd(current, table):
    for i in range(current, len(table)):
        if table[i]:
            return False

    return True


def solution(n, k, cmd):
    if n == 1:
        return "O"
    answer = ''
    selected = k
    recent_deleted_list = []
    table = [True] * n
    print(table)

    for aCmd in cmd:
        if aCmd[0] == "D":
            # 현재 선택된 행에서 aCmd[2] 아래에 있는 행 선택
            selected = down(selected, int(aCmd[2]), table)

        elif aCmd[0] == "U":
            # 현재 선택된 행에서 aCmd[2] 위에 있는 행 선택
            # upCount = 0
            # temp = 0
            # while True:
            #     if upCount == int(aCmd[2]):
            #         selected -= temp
            #         break
            #     if table[selected - temp]:
            #         upCount += 1
            #     temp += 1
            selected = up(selected, int(aCmd[2]), table)
        elif aCmd[0] == "C":
            # 현재 선택행 삭제후 바로 아래행 선택
            # 삭제된 행이 가장 마지막일 경우 바로 윗행 선택
            recent_deleted_list.append(selected)
            table[selected] = False
            if isEnd(selected, table):
                selected = up(selected, 1, table)
            else:
                selected = down(selected, 1, table)

        elif aCmd[0] == "Z":
            # 되돌리기!
            table[recent_deleted_list.pop()] = True

    for t in table:
        if t:
            answer += "O"
        else:
            answer += "X"
    return answer


if __name__ == "__main__":
    arr_n = [30, 8, 10]
    arr_k = [2, 2, 2]
    arr_cmd = [["D 20", "C"],
               ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"],
               ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z","C"]]

    for n, k, cmd in zip(arr_n, arr_k, arr_cmd):
        print(solution(n, k, cmd))
