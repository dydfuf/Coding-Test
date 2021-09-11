from itertools import combinations_with_replacement


# 2포인터로 풀 수 있을듯 일단 combination으로 풀자
def solution(student, k):
    answer = 0

    length = len(student)

    temp = [i for i in range(length)]

    for comb in combinations_with_replacement(temp, 2):

        if sum(student[comb[0]:comb[1]+1]) == k:
            answer += 1

    return answer


if __name__ == '__main__':
    arr_student = [[0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0], [0, 1, 0]]
    arr_k = [1, 2, 2]
    arr_result = [6, 8, 0]

    for student, k, result in zip(arr_student, arr_k, arr_result):
        print(solution(student,k), result)
