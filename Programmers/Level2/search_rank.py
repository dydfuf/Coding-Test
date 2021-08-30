from itertools import combinations

def solution(info, query):
    answer = []

    infoDict = {}

    for aInfo in info:
        splitInfo = aInfo.split(" ")

        key = splitInfo[:-1]
        score = int(splitInfo[-1])

        for i in range(5):
            for c in combinations(key,i):
                temp = "".join(c)
                if temp in infoDict:
                    infoDict[temp].append(score)
                else:
                    infoDict[temp] = [score]

    for value in infoDict.values():
        value.sort()

    for aQuery in query:

        splitQuery = [i for i in aQuery.split() if not i in ["and", "-"]]

        aScore = int(splitQuery[-1])
        aQuery = "".join(splitQuery[:-1])

        if aQuery in infoDict:

            resultSet = infoDict[aQuery]

            start, end = 0, len(resultSet)
            while start < end:
                mid = (start + end) // 2
                if resultSet[mid] >= aScore:
                    end = mid
                else:
                    start = mid + 1

            answer.append(len(resultSet) - start)
        else:
            answer.append(0)


    return answer


if __name__ == '__main__':
    info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
            "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
             "- and - and - and chicken 100", "- and - and - and - 150"]
    result = [1, 1, 1, 1, 2, 4]

    print(solution(info, query), result)
