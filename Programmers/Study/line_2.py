def solution(research, n, k):
    search_alpha = set()
    _dict = dict()
    for r in research:
        for c in r:
            search_alpha.add(c)

    search_alpha = list(search_alpha)
    search_alpha.sort()

    for alpha in search_alpha:
        _dict[alpha] = []
        for r in research:
            _dict[alpha].append(r.count(alpha))

    length = len(research)

    _answer = dict()

    for i in range(length - n + 1):
        for key in _dict.keys():
            temp = _dict[key]
            if sum(temp[i:i + n]) < 2 * n * k:
                continue

            v = True
            for j in range(i, i + n):
                if temp[j] < k:
                    v = False
                    break

            if v:
                if key in _answer.keys():
                    _answer[key] += 1
                else:
                    _answer[key] = 1

    listAnswer = []

    for key in _answer.keys():
        listAnswer.append([key, _answer[key]])

    listAnswer.sort(key=lambda x: (int(-x[1]), x[0]))

    if listAnswer:
        return listAnswer[0][0]
    else:
        return "None"




if __name__ == '__main__':
    arr_research = [["abaaaa", "aaa", "abaaaaaa", "fzfffffffa"], ["yxxy", "xxyyy"], ["yxxy", "xxyyy", "yz"],
                    ["xy", "xy"]]
    arr_n = [2, 2, 2, 1]
    arr_k = [2, 1, 1, 1]
    arr_result = ["a", "x", "y", "None"]

    for research, n, k, result in zip(arr_research, arr_n, arr_k, arr_result):
        print(solution(research, n, k), result)
