
def solution(land):
    dp = land

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            temp = dp[ i -1].copy()
            temp.pop(j)

            dp[i][j] += max(temp)

    return max(dp[-1])


if __name__ == '__main__':
    land = [[1 ,2 ,3 ,5] ,[5 ,6 ,7 ,8] ,[4 ,3 ,2 ,1]]
    print(solution(land))
