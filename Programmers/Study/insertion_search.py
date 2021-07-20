def solution(sorting_list):
    for i in range(1, len(sorting_list)):
        k = sorting_list[i]

        for j in range(0, i):
            if sorting_list[j] > k:
                sorting_list.pop(i)
                sorting_list.insert(j, k)
                break

    return sorting_list


if __name__ == "__main__":
    sorting_list = [5, 4, 3, 2, 1, 8, 7, 9, 6,1]
    print(solution(sorting_list))
