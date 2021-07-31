def solution(s):
    if not s:
        return ""
    answer = ''
    s = s.lower()
    split_s = s.split(" ")

    for word in split_s:
        temp = word.capitalize()
        answer += temp+" "

    return answer[:-1]


if __name__ == '__main__':
    arr_s = [" 3       unFollowed      me", "for the last week"]
    for s in arr_s:
        print(solution(s))
