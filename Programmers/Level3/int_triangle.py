def solution(triangle):

    length = len(triangle)

    for i in range(1, length):
        rowLen = len(triangle[i])
        for j in range(rowLen):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == rowLen-1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    return max(triangle[-1])


if __name__ == '__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	))