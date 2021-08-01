def solution(A, B):
    A = sorted(A)
    B = sorted(B, reverse=True)

    result = 0
    for a, b in zip(A, B):
        result += a*b

    return result


if __name__ == "__main__":
    arr_A = [[1, 4, 2], [1, 2]]
    arr_B = [[5, 4, 4], [3, 4]]
    for A, B in zip(arr_A, arr_B):
        print(solution(A, B))