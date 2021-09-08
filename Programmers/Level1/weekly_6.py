def solution(weights, head2head):
    answer = []

    numPeople = len(weights)

    sortArr = []
    i = 1
    for aWeight, aHead2Head in zip(weights, head2head):

        # win rate
        winCount = aHead2Head.count("W")
        nCount = aHead2Head.count("N")
        if numPeople == nCount:
            winRate = 0
        else:
            winRate = winCount / (numPeople - nCount)

        # win count heavier people
        winCountHeavier = 0
        for idx, rate in enumerate(aHead2Head):
            if rate == "W" and aWeight < weights[idx]:
                winCountHeavier += 1

        sortArr.append([winRate, winCountHeavier, aWeight, i])
        i += 1

    sortArr.sort(key=lambda x: (-float(x[0]), -int(x[1]), -int(x[2]), int(x[3])))

    for aArr in sortArr:
        answer.append(aArr[3])

    return answer


if __name__ == '__main__':
    arr_weights = [[50, 82, 75, 120], [145, 92, 86], [60, 70, 60]]
    arr_head2head = [["NLWL", "WNLL", "LWNW", "WWLN"], ["NLW", "WNL", "LWN"], ["NNN", "NNN", "NNN"]]
    arr_result = [[3, 4, 1, 2], [2, 3, 1], [2, 1, 3]]
    for weights, head2head, result in zip(arr_weights, arr_head2head, arr_result):
        print(solution(weights, head2head), result)
