import sys

input = sys.stdin.readline
import heapq

if __name__ == "__main__":
    N, M, X = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    INF = int(1e9)
    distance = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        for j in range(N + 1):
            if i == j:
                distance[i][j] = 0

    for _ in range(M):
        a, b, t = map(int, input().split())
        graph[a].append([b, t])


    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))

        while q:
            dist, now = heapq.heappop(q)

            if distance[start][now] < dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[start][i[0]]:
                    distance[start][i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))


    for i in range(1, N + 1):
        dijkstra(i)

    answer = 0

    for i in range(1, N + 1):
        temp = distance[i][X] + distance[X][i]
        if temp > answer:
            answer = temp

    print(answer)
