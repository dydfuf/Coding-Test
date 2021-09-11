def solution(board, skill):
    answer = 0

    for aSkill in skill:
        skillType, r1, c1, r2, c2, degree = aSkill

        if skillType == 1:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    board[i][j] -= degree
        else:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    board[i][j] += degree

    N = len(board)
    M = len(board[0])

    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                answer += 1

    return answer


if __name__ == '__main__':
    arr_board = [[[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,2,3],[4,5,6],[7,8,9]]]
    arr_skill = [[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]]
    arr_result = [10, 6]

    for board, skill, result in zip(arr_board, arr_skill, arr_result):
        print(solution(board, skill), result)