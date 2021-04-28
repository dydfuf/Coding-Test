def solution(s):
    answer = 0
    small = []
    middle = []
    large = []
    stack = []
    if len(s) % 2 == 1:
        return 0

    for i in range(len(s)):
        new_s = s[i:] + s[:i]
        for aS in new_s:
            if aS in ["(", "{", "["]:
                stack.append(aS)
            elif aS == ")":
                if not stack:
                    break
                elif stack[-1] == "(":
                    stack.pop()
            elif aS == "}":
                if not stack:
                    break
                elif stack[-1] == "{":
                    stack.pop()
            elif aS == "]":
                if not stack:
                    break
                elif stack[-1] == "[":
                    stack.pop()
        else:
            if not stack:
                answer += 1

    return answer


if __name__ == "__main__":
    arr_s = [
        "[](){}",
        "}]()[{",
        "[)(]",
        "}}}",
        "[(])"
    ]
    for s in arr_s:
        print(solution(s))