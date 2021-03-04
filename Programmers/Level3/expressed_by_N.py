def solution(N, number):
    answer = - 1
    DP = []
    for i in range(1, 9):
        case_set = {int(str(N) * i)}

        for j in range(0, i - 1):
            for x in DP[j]:
                for y in DP[-j - 1]:
                    case_set.add(x + y)
                    case_set.add(x - y)
                    case_set.add(x * y)
                    if y != 0:
                        case_set.add(x // y)
        if number in case_set:
            return i

        DP.append(case_set)
    return answer


N = 5
number = 12
print(solution(N, number))

N = 2
number = 22
print(solution(N, number))
