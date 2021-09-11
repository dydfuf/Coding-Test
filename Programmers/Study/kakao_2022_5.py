from collections import deque

def solution(info, edges):
    answer = 0

    graph = dict()

    for i in range(len(edges)):
        graph[i] = []

    for edge in edges:
        graph[edge[0]].append(edge[1])

    candidate = deque()
    ccc = list()
    for i in graph[0]:
        candidate.append([i, 0, 1, 0])
        ccc.append(str(i)+" 0 1 0")

    visited = [0] * len(info)

    while ccc:
        tempStr = ccc[0]
        ccc.pop(0)
        nxt, now, ns, nw = map(int, tempStr.split(" "))

        visited[now] = 1
        if ns > answer:
            answer = ns

        if sum(visited) == len(info):
            break

        if info[nxt] == 0:
            ns += 1
        else:
            nw += 1

        ts = []
        for cand in ccc:
            _nxt, _now, _ns, _nw = map(str, cand.split(" "))
            temp = _nxt + " " + str(nxt) + " " + str(ns) + " " + str(nw)
            if _nxt != str(nxt) and _now != str(nxt) and temp not in ccc:
                ts.append(temp)

        for t in ts:
            if t not in ccc:
                ccc.append(t)

        if nxt in graph.keys():
            for i in graph[nxt]:
                temp = str(i) + " " + str(nxt) + " " + str(ns) + " " + str(nw)
                if temp not in ccc:
                    ccc.append(temp)

    return answer


if __name__ == '__main__':
    arr_info = [[0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
    arr_edges = [[[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]],
                 [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]]
    arr_result = [5, 5]

    for info, edges, result in zip(arr_info, arr_edges, arr_result):
        print(solution(info, edges), result)
