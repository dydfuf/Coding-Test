def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5] * 2000
    ans_one = 0
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    ans_two = 0
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    ans_three = 0

    for i in range(0, len(answers)):
        if answers[i] == one[i]:
            ans_one += 1
        if answers[i] == two[i]:
            ans_two += 1
        if answers[i] == three[i]:
            ans_three += 1

    max_problem = max(ans_one, ans_two, ans_three)
    if ans_one == max_problem:
        answer.append(1)
    if ans_two == max_problem:
        answer.append(2)
    if ans_three == max_problem:
        answer.append(3)
    return answer


if __name__ == "__main__":
    answers = [1, 3, 2, 4, 2]
    print(solution(answers))
