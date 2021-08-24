def reArrange(arr, m, n):
    for _ in range(m):
        for i in range(m - 1):
            for j in range(n):
                if arr[i][j] != "0" and arr[i + 1][j] == "0":
                    arr[i + 1][j] = arr[i][j]
                    arr[i][j] = "0"

    return arr


def solution(m, n, board):
    answer = 0

    board = [list(i) for i in board]

    while True:
        popCheck = False

        temp = list()

        # deep copy
        for i in range(m):
            a = list()
            for j in range(n):
                a.append(board[i][j])
            temp.append(a)

        for i in range(m - 1):
            for j in range(n - 1):
                cur = board[i][j]

                if cur != "0" and cur == board[i + 1][j] and cur == board[i][j + 1] and cur == board[i + 1][j + 1]:
                    temp[i][j] = "0"
                    temp[i + 1][j] = "0"
                    temp[i][j + 1] = "0"
                    temp[i + 1][j + 1] = "0"
                    popCheck = True

        board = reArrange(temp, m, n)

        if not popCheck:
            break

    for i in board:
        s = "".join(i)
        answer += s.count("0")
    return answer


if __name__ == '__main__':
    arr_m = [4, 6]
    arr_n = [5, 6]
    arr_board = [["CCBDE", "AAADE", "AAABF", "CCBBF"], ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]]
    arr_answer = [14, 15]

    for m, n, board, answer in zip(arr_m, arr_n, arr_board, arr_answer):
        print(solution(m, n, board), answer)

    m = 6
    n = 6
    board = ['AABBEE', 'AAAEEE', 'VAAEEV', 'AABBEE', 'AACCEE', 'VVCCEE']
    print(solution(m, n, board))  # 32
