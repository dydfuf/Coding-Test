def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x * i)
    return answer


if __name__ == "__main__":
    arr_x = [2, 4, -4]
    arr_n = [5, 3, 2]
    for x, n in zip(arr_x, arr_n):
        print(solution(x, n))
