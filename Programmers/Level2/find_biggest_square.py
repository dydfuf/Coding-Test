def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] != 0:
                # 0이 아닌지 조건문을 안건 이유는 MIN을 하면 어차피 0이 MIN이므로!
                board[i][j] = min(board[i - 1][j], board[i - 1][j-1], board[i][j - 1]) + 1

    result = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            result.append(board[i][j])

    return max(result)**2


if __name__ == '__main__':
    arr_board = [[[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]], [[0, 0, 1, 1], [1, 1, 1, 1]]]
    for board in arr_board:
        print(solution(board))
