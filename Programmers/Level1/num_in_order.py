def solution(n):
    answer = ""
    ans_list = []
    for c in str(n):
        ans_list.append(int(c))

    ans_list.sort(reverse=True)

    for i in ans_list:
        answer += str(i)

    return int(answer)


if __name__ == "__main__":
    n = 118372
    print(solution(n))