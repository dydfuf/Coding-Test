import heapq

def solution(n, works):
    answer = 0
    if n > sum(works):
        return 0

    works = [-w for w in works]

    heapq.heapify(works)

    for _ in range(n):
        heapq.heappush(works, heapq.heappop(works) + 1)

    for aWork in works:
        answer += aWork * aWork

    return answer


if __name__ == '__main__':
    arr_works = [[4, 3, 3], [2, 1, 2], [1, 1], [1, 1, 1], [2, 16, 22, 55, 55]]
    arr_n = [4, 1, 3, 9, 99]
    for n, works in zip(arr_n, arr_works):
        print(solution(n, works))
