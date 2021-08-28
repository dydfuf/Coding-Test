def solution(a):
    answer = []

    for aA in a:
        while True:
            print(aA)
            if len(aA) == 1:
                if aA == "a":
                    answer.append(True)
                else:
                    answer.append(False)
                break

            if aA[0] == aA[-1] == "b":
                bLength = 0
                for i in range(len(aA)):
                    if aA[i] == aA[-1-i] == "b":
                        bLength += 1
                    else:
                        break
                if aA.count("a") == bLength:
                    aA = aA[bLength:-bLength]
                else:
                    answer.append(False)
                    break
            elif aA[0] == "a":
                aA = aA[1:]
            elif aA[-1] == "a":
                aA = aA[:-1]

    return answer


if __name__ == '__main__':
    a = ["abab", "bbaa", "bababa", "bbbabababbbaa", "bbbbbaabbabbb"]
    result = [True, False, False, True, True]
    print(solution(a), result)
