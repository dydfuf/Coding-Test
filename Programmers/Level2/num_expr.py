def solution(n):
    answer = 0

    for i in range(1, n):
        temp = i
        for j in range(i + 1, n):
            temp += j
            if temp == n:
                answer += 1
                # print(i, j)
            elif temp > n:
                break
            else:
                continue

    return answer+1


if __name__ == '__main__':
    arr_n = [15]
    for n in arr_n:
        print(solution(n))
