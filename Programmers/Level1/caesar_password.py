def solution(s, n):
    answer = ''
    for c in s:
        if c.isupper():
            c = chr((ord(c) - ord('A') + n) % 26 + ord('A'))
        elif c.islower():
            c = chr((ord(c) - ord('a') + n) % 26 + ord('a'))
        answer += c

    return answer


if __name__ == "__main__":
    s = "AB"
    n = 1
    print(solution(s, n))
    s = "z"
    n = 1
    print(solution(s, n))
    s = "a B Z"
    n = 4
    print(solution(s, n))