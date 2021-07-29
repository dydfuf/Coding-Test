def solution(arr1, arr2):
    # AXB * BXC = AXC
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer


if __name__ == "__main__":
    arr1_arr = [[[1, 4], [3, 2], [4, 1]], [[2, 3, 2], [4, 2, 4], [3, 1, 4]]]
    arr2_arr = [[[3, 3], [3, 3]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]]
    for arr1, arr2 in zip(arr1_arr, arr2_arr):
        print(solution(arr1, arr2))
