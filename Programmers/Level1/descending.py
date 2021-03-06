def solution(s):
    answer = ''
    return ''.join(reversed(sorted(s)))

if __name__ == "__main__":
    s = "Zbcdefg"
    print(solution(s))