def solution(s):
    answer = 0

    stack = []
    for aS in s:
        if stack:
            if aS == stack[-1]:
                stack.pop()
            else:
                stack.append(aS)
        else:
            stack.append(aS)
    if stack:
        return 0
    else:
        return 1

    return answer

if __name__ == "__main__":
    arr_s = [
        "baaabaa",
        "cdcd",
        "cbbaac"
    ]
    for s in arr_s:
        print(solution(s))
