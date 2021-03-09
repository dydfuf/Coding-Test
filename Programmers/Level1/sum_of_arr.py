def sum_list(list1, list2):
    result = []
    for l1, l2 in zip(list1, list2):
        result.append(l1 + l2)
    return result


def solution(arr1, arr2):
    answer = []

    for a1, a2 in zip(arr1, arr2):
        answer.append(sum_list(a1, a2))

    return answer


if __name__ == "__main__":
    arr1 = [[1,2],[2,3]]
    arr2 = [[3,4],[5,6]]
    print(solution(arr1, arr2))
    arr1 = [[1],[2]]
    arr2 = [[3],[4]]
    print(solution(arr1, arr2))