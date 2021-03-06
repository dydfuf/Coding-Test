def solution(s):
    answer = ''

    if len(s) % 2 == 1:
        answer = s[len(s) // 2]
    else:
        answer += s[len(s) // 2 - 1] + s[len(s) // 2]
    return answer

if __name__ == "__main__":
    s = "abcd"
    print(solution(s))