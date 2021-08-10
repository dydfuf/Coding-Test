def solution(dirs):
    answer = 0
    position = [5, 5]
    hist = []
    for dir in dirs:
        start = position
        if dir == "U":
            if position[0] - 1 > -1:
                position = [position[0] - 1, position[1]]
        elif dir == "L":
            if position[1] - 1 > -1:
                position = [position[0], position[1] - 1]
        elif dir == "R":
            if position[1] + 1 < 11:
                position = [position[0], position[1] + 1]
        else:
            if position[0] + 1 < 11:
                position = [position[0] + 1, position[1]]
        dest = position
        if [start, dest] not in hist and [dest, start] not in hist and not start == dest:
            answer += 1
            # print("--", [start, dest])
            hist.append([start, dest])
            hist.append([dest, start])

    return answer


if __name__ == '__main__':
    arr_dirs = ["ULURRDLLU", "LULLLLLLU", "RRRRRRRRRR"]
    for dirs in arr_dirs:
        print(solution(dirs))
