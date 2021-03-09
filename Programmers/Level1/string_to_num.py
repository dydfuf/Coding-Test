def solution(s):

    if s[0] == "-":
        return int(s[1:])*(-1)
    else:
        return int(s)


if __name__ == "__main__":
    s = "1234"
    print(solution(s))
    s = "-1234"
    print(solution(s))