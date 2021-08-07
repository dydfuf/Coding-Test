def solution(s):
    check = 0

    for aS in s:
        if check == 0 and aS == ")":
            return False
        if aS == "(":
            check += 1
        if aS == ")":
            check -= 1

    if check == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    arr_s = ["()()", "(())()", ")()(", "(()("]
    for s in arr_s:
        print(solution(s))
