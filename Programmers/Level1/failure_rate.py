def solution(N, stages):
    answer = []
    stages.sort()

    failure = [0] * (N+1)

    for item in stages:
        for i in range(0, item):
            failure[i] += 1

    failure_rate = []
    for i in range(0, len(failure)-1):
        try:
            failure_rate.append((failure[i] - failure[i+1])/failure[i])
        except ZeroDivisionError:
            failure_rate.append(0)

    f_list = []
    for i in range(0, len(failure_rate)):
        f_list.append([i+1, failure_rate[i]])

    f_list.sort(key=lambda x: x[1], reverse=True)
    for stage in f_list:
        answer.append(stage[0])
    return answer


if __name__ == "__main__":
    arr_N = [5, 4, 5]
    arr_stages = [[2, 1, 2, 6, 2, 4, 3, 3], [4, 4, 4, 4, 4], [2,1,2,4,2,4,3,3]]
    for N, stages in zip(arr_N, arr_stages):
        print(solution(N, stages))
