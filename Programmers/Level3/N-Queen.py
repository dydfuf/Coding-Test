def dfs(queens, next_queen, n, answer):
    if next_queen in queens:
        return

    for row, col in enumerate(queens):
        h = len(queens) - row
        if next_queen == col + h or next_queen == col-h:
            return

    queens.append(next_queen)

    if len(queens) == n:
        answer[0] += 1
        return

    for next_queen in range(n):
        dfs(queens[:], next_queen, n, answer)



def solution(n):
    answer = [0]
    for next_queen in range(n):
        queens = []
        dfs(queens, next_queen, n, answer)

    return answer[0]


if __name__ == '__main__':
    print(solution(4), 2)
    print(solution(12))
