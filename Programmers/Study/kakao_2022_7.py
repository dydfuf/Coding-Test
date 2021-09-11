def solution(board, aloc, bloc):
    answer = -1
    return answer


if __name__ == '__main__':
    arr_board = [[[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 1, 1, 1, 1]], [[1]]]
    arr_aloc = [[1, 0], [1, 0], [0, 0], [0, 0]]
    arr_bloc = [[1, 2], [1, 2], [0, 4], [0, 0]]
    arr_result = [5, 4, 4, 0]

    for board, aloc, bloc, result in zip(arr_board, arr_aloc, arr_bloc, arr_result):
        print(solution(board, aloc, bloc), result)