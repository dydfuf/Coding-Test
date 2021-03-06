def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        move = move-1
        for bo in board:
            if bo[move] != 0:
                if len(stack) == 0:
                    stack.append(bo[move])
                elif stack[len(stack)-1] == bo[move]:
                    stack.pop()
                    answer+=2
                elif stack[len(stack)-1] != bo[move]:
                    stack.append(bo[move])
                bo[move] = 0
                break
    return answer


if __name__ == "__main__":
    board = [[0, 0, 0, 0, 0],
             [0, 0, 1, 0, 3],
             [0, 2, 5, 0, 1],
             [4, 2, 4, 4, 2],
             [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    print(solution(board, moves))
