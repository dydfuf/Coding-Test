def solution(n):
    answer = [[0 for _ in range(1, i+1)] for i in range(1, n+1)]

    x, y = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
    return sum(answer, [])


if __name__ == '__main__':
    arr_n = [4, 5, 6]
    arr_result = [[1, 2, 9, 3, 10, 8, 4, 5, 6, 7], [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9],
                  [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11]]
    for n, result in zip(arr_n, arr_result):
        print(solution(n), result)
