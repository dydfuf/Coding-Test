def solution(str1, str2):
    answer = 0

    str1 = str1.lower()
    str2 = str2.lower()
    str1_list = [i for i in str1]
    str2_list = [i for i in str2]

    jSet1 = []
    jSet2 = []
    for i in range(len(str1_list) - 1):
        if str1_list[i].isalpha() and str1_list[i + 1].isalpha():
            jSet1.append(str1_list[i] + str1_list[i + 1])

    for i in range(len(str2_list) - 1):
        if str2_list[i].isalpha() and str2_list[i + 1].isalpha():
            jSet2.append(str2_list[i] + str2_list[i + 1])

    if len(jSet1) == 0 and len(jSet2) == 0:
        return 65536

    if len(jSet1) > len(jSet2):
        inner = [jSet1.remove(x) for x in jSet2 if x in jSet1]
    else:
        inner = [jSet2.remove(x) for x in jSet1 if x in jSet2]

    union = len(jSet1 + jSet2)

    if union == 0:
        return 65536

    return int(len(inner)/union * 65536)

if __name__ == '__main__':
    arr_str1 = ["FRANCE", "handshake", "aa1+aa2", "E=M*C^2", "aaa"]
    arr_str2 = ["french", "shake hands", "AAAA12", "e=m*c^2", "aabbcde"]
    for str1, str2 in zip(arr_str1, arr_str2):
        print(solution(str1, str2))
