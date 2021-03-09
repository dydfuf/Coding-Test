def solution(s):
    answer = ''

    words = s.split(' ')
    for word in words:
        for i in range(0, len(word)):
            if i % 2 == 0:
                c = word[i].upper()
            elif i % 2 == 1:
                c = word[i].lower()
            answer += c
        answer += " "
    if answer[len(answer)-1] == ' ':
        answer = answer[0:len(answer)-1]
    return answer


if __name__ == "__main__":
    s = "trye hello world"
    print(solution(s))