def checkValidParen(str):
    isValid = True

    stack = []
    for a in str:
        if a == "(":
            stack.append("(")
        else:
            if not stack:
                isValid = False
                break
            stack.pop()

    return isValid


def splitUV(str):
    count = 0
    u = ''
    v = ''
    for a in str:
        if a == "(":
            count += 1
        else:
            count -= 1
        u += a
        if count == 0:
            break
    v = str[len(u):]

    return u, v


def solution(p):
    answer = ''
    stack = [p]

    # step 1
    if not p:
        return p

    # step 1-1 이미 올바른 괄호 문자열이라면 리턴
    if checkValidParen(p):
        return p

    # step 2
    u, v = splitUV(p)

    # step 3
    if checkValidParen(u):
        # step 3-1
        return u + solution(v)
    else:
        answer += "("
        answer += solution(v)
        answer += ")"

    u = u[1:-1]
    for i in u:
        if i == "(":
            answer += ")"
        else:
            answer += "("
    return answer


if __name__ == "__main__":
    arr_p = [
        "(()())()",
        ")(",
        "()))((()",
        ""
    ]
    for p in arr_p:
        print(solution(p))

