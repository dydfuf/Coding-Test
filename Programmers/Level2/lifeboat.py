from collections import deque


def solution(people, limit):
    answer = 0

    people.sort(reverse=True)

    deq = deque(people)

    while deq:
        if len(deq) == 1:
            answer += 1
            break
        if deq[0] + deq[-1] > limit:
            deq.popleft()
        else:
            deq.popleft()
            deq.pop()
        answer += 1

    return answer


if __name__ == '__main__':
    arr_people = [[70, 50, 80, 50], [70, 80, 50], [40, 50, 150, 160], [100, 500, 500, 900, 950], [40, 50, 60, 90]]
    arr_limit = [100, 100, 200, 1000, 100]
    arr_return = [3, 3, 2, 3, 3]

    for people, limit, result in zip(arr_people, arr_limit, arr_return):
        print(solution(people, limit), result)
