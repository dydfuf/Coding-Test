def solution(d, budget):
    answer = 0
    d = sorted(d)

    sum_of_item = 0
    for i in d:
        if sum_of_item + i > budget:
            break
        sum_of_item += i
        answer += 1

    return answer


if __name__ == "__main__":
    arr_d = [[1, 3, 2, 5, 4], [2, 2, 3, 3]]
    arr_budget = [9, 10]
    for d, budget in zip(arr_d, arr_budget):
        print(solution(d, budget))
