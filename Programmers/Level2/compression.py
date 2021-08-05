def findLongestSubsetInDict(msg, dictionary, startIdx):
    if msg[startIdx] not in dictionary:
        return startIdx

    result = len(msg)
    temp = msg[startIdx]
    for i in range(startIdx + 1, len(msg)):
        temp += msg[i]
        if temp not in dictionary:
            result = i
            break

    return result


def solution(msg):
    answer = []

    # 사전 초기화 색인 번호를 맞추기 위해 0번째 idx에 임의의값
    dictionary = [0]
    for i in range(65, 91):
        dictionary.append(str(chr(i)))

    idx = 0
    while True:
        # 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
        end = findLongestSubsetInDict(msg, dictionary, 0)
        w = msg[0:end]
        if not end == len(msg):
            c = msg[end]
            # w에 해당하는 사전의 색인 번호를 출력하고 입력에서 w를 제거한다.
            answer.append(dictionary.index(w))
            dictionary.append(w + c)
            msg = msg[end:]
        else:
            answer.append(dictionary.index(w))
            break

    return answer


if __name__ == '__main__':
    arr_msg = ["KAKAO", "TOBEORNOTTOBEORTOBEORNOT", "ABABABABABABABAB"]
    for msg in arr_msg:
        print(solution(msg))
