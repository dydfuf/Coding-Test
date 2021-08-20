def solution(begin, target, words):
    if target not in words:
        return 0

    length = len(words)

    graph = [[0 for _ in range(length)] for _ in range(length)]

    for i in range(length):
        for j in range(length):
            diff = 0
            for c, w in zip(words[i], words[j]):
                if c != w:
                    diff += 1

            if diff == 1:
                graph[i][j] = 1

    first = [False for _ in range(length)]

    for i in range(length):
        diff = 0
        for c, w in zip(begin, words[i]):
            if c != w:
                diff += 1

        if diff == 1:
            first[i] = True

    result = []

    def dfs(graph, visited, i, count):
        if words[i] == target:
            result.append(count)
            return
        length = len(graph[i])
        for j in range(length):
            if graph[i][j] == 1 and i != j and not visited[j]:
                visited[j] = True
                dfs(graph, visited, j, count + 1)
                visited[j] = False

        return

    for i in range(length):
        if first[i]:
            # dfs start i
            visited = [False for _ in range(length)]
            visited[i] = True
            dfs(graph, visited, i, 1)

    return min(result)


if __name__ == '__main__':
    arr_begin = ["hit", "hit"]
    arr_target = ["cog", "cog"]
    arr_words = [["hot", "dot", "dog", "lot", "log", "cog"],
                 ["hot", "dot", "dog", "lot", "log"]]
    for begin, target, words in zip(arr_begin, arr_target, arr_words):
        print(solution(begin, target, words))
