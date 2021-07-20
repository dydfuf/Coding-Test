import pprint


def solution(rows, columns, queries):
    answer = []

    initArr = list()
    for i in range(rows + 1):
        row = [j + ((i - 1) * columns) for j in range(columns + 1)]
        initArr.append(row)
    # rotate

    for query in queries:
        # 오른쪽 위를 빼자
        temp = initArr[query[0]][query[3]]
        border_num_list = list()
        # 상 move
        # print("up")
        for i in range(query[3] - 1, query[1] - 1, -1):
            initArr[query[0]][i + 1] = initArr[query[0]][i]
            # print(query[0], i, "to", query[0], i + 1)
            border_num_list.append(initArr[query[0]][i])
        # 좌 move
        # print("left")
        for i in range(query[0] + 1, query[2] + 1):
            initArr[i - 1][query[1]] = initArr[i][query[1]]
            # print(i, query[1], "to", i - 1, query[1])
            border_num_list.append(initArr[i][query[1]])

        # 하 move
        # print("down")
        for i in range(query[1] + 1, query[3] + 1):
            initArr[query[2]][i - 1] = initArr[query[2]][i]
            # print(query[2], i, "to", query[2], i - 1)
            border_num_list.append(initArr[query[2]][i])
        # 우 move
        # print("right")
        for i in range(query[2] - 1, query[0], -1):
            initArr[i + 1][query[3]] = initArr[i][query[3]]
            # print(i, query[3], "to", i + 1, query[3])
            border_num_list.append(initArr[i][query[3]])
        initArr[query[0] + 1][query[3]] = temp
        border_num_list.append(temp)
        # print(initArr[1:])
        # print(border_num_list)
        # print(min(border_num_list))
        answer.append(min(border_num_list))
    return answer


if __name__ == "__main__":
    arr_rows = [6, 3, 100]
    arr_columns = [6, 3, 97]
    arr_queries = [[[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]],
                   [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]],
                   [[1, 1, 100, 97]]]

    for rows, columns, queries in zip(arr_rows, arr_columns, arr_queries):
        print(solution(rows, columns, queries))
