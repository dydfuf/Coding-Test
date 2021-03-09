def solution(dartResult):
    answer = 0

    a_list = []

    for i in range(0, len(dartResult)):
        if dartResult[i] in ["S", "D", "T", "*", "#"]:
            a_list.append([dartResult[i], i])

    idx = 0
    three = []
    for aList in a_list:
        if aList[0] == "S":
            three.append(int(dartResult[idx:aList[1]]) ** 1)
            idx = aList[1]+1
        elif aList[0] == "D":
            three.append(int(dartResult[idx:aList[1]]) ** 2)
            idx = aList[1]+1
        elif aList[0] == "T":
            three.append(int(dartResult[idx:aList[1]]) ** 3)
            idx = aList[1]+1
        elif aList[0] == "*":
            three[-1] *= 2
            if len(three) >= 2:
                three[-2] *= 2
            idx = aList[1]+1
        elif aList[0] == "#":
            three[-1] *= -1
            idx = aList[1]+1

    answer = sum(three)
    return answer


if __name__ == "__main__":
    arr_dartResult = ["1S2D*3T", "1D2S#10S", "1D2S0T", "1S*2T*3S",
                      "1D#2S*3S", "1T2D3D#", "1D2S3T*"]
    for dartResult in arr_dartResult:
        print(solution(dartResult))