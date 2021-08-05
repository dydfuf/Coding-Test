def solution(files):
    answer = []
    HNT = []
    for file in files:
        head = ""
        number = ""
        tail = ""
        idx = 0
        for i in range(len(file)):
            if not file[i].isnumeric():
                head += file[i]
            else:
                idx = i
                break
        notBreak = False
        for i in range(idx, len(file)):
            if file[i].isnumeric():
                number += str(file[i])
            else:
                idx = i
                break
        else:
            notBreak  = True

        tail = file[idx:]

        if notBreak:
            tail = ""
        HNT.append([head, number, tail])
    HNT = sorted(HNT, key=lambda x: (x[0].lower(), int(x[1])))
    for aHNT in HNT:
        toAnswer = ""
        for indHNT in aHNT:
            toAnswer += indHNT
        answer.append(toAnswer)

    return answer


if __name__ == '__main__':
    arr_files = [["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG", "foo010bar020.zip", "F-15"],
                 ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]]
    for files in arr_files:
        print(solution(files))
