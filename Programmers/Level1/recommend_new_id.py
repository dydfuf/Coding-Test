def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    second = []
    for idx, aNewId in enumerate(new_id):
        if aNewId.isalpha():
            continue
        if aNewId.isnumeric():
            continue
        if aNewId in ["-", "_", "."]:
            continue
        second.append(idx)

    second.reverse()

    temp = list(new_id)

    for i in second:
        temp.pop(i)

    new_id = ''.join(temp)

    # 3단계
    temp = list(new_id)
    third = list()
    for idx, aTemp in enumerate(temp):
        if idx == len(temp) - 1:
            break
        if aTemp == ".":
            if temp[idx + 1] == ".":
                third.append(idx + 1)

    third.reverse()
    for i in third:
        temp.pop(i)
    new_id = ''.join(temp)

    # 4단계
    temp = list(new_id)
    if temp[0] == ".":
        temp.pop(0)
    if temp and temp[-1] == ".":
        temp.pop()

    new_id = ''.join(temp)

    # 5단계
    if not temp:
        new_id = "a"

    # 6단계
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    if len(new_id) < 3:
        if len(new_id) == 1:
            new_id = new_id[0] * 3
        else:
            new_id += new_id[-1]
    return new_id


if __name__ == "__main__":
    arr_new_id = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=", "123_.def", "abcdefghijklmn.p"]
    for new_id in arr_new_id:
        print(solution(new_id))
