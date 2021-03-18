def checkStack(stack):
    # i개의 엘리먼트가 있는 스택이라고 가정 할때
    # i-2, i-1, i를 비교
    # i-1 > i-2 and i-1 > i 이면 pop(i)

    while True:
        if len(stack) < 3:
            break

        if stack[len(stack)-2] > stack[len(stack) - 3] and stack[len(stack)-2] > stack[len(stack)-1]:
            stack.pop(len(stack) - 2 )
        else:
            break

    return stack


def solution(a):
    answer = 0
    # 반드시 지워질 것을 먼저 지우자!
    st = [a[0], a[1]]
    a.pop(0)
    a.pop(0)
    for aA in a:
        st.append(aA)
        st = checkStack(st)

    return len(st)


if __name__ == "__main__":
    arr_a = [[9, -1, -5], [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]]
    for a in arr_a:
        print(solution(a))