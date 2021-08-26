import heapq

def solution(N, road, K):
    answer = 0

    INF = 5000000
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)

    for aRoad in road:
        a, b, c = aRoad
        graph[a].append([b,c])
        graph[b].append([a,c])

    def dijkstra(start):
        q = []
        distance[start] = 0
        heapq.heappush(q, (0, start))

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(1)

    for i in distance:
        if i <= K:
            answer += 1

    return answer

if __name__ == '__main__':
    arr_N = [5, 6]
    arr_road = [[[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]],
                [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]]
    arr_K = [3, 4]
    arr_result = [4, 4]

    for N, road, K, result in zip(arr_N, arr_road, arr_K, arr_result):
        print(solution(N, road, K), result)
