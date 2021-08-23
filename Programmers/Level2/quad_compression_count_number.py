def solution(arr):
    answer = [0, 0]
    length = len(arr)

    def divide(x, y, n):
        default = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y+n):
                if arr[i][j] != default:

                    nn = n // 2
                    divide(x, y, nn)
                    divide(x, y + nn, nn)
                    divide(x+nn, y, nn)
                    divide(x+nn, y+nn, nn)
                    return
        answer[default] += 1

    divide(0, 0, length)

    return answer


if __name__ == "__main__":
    arr_arr = [[[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]],
               [[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]]
    for arr in arr_arr:
        print(solution(arr))
