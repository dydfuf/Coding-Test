def solution(number, k):
    stack = [number[0]]

    for num in number[1:]:
        while len(stack) > 0and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)

    if k != 0:
        stack = stack[:-k]
    answer = ''.join(stack)
    return answer


if __name__ == "__main__":
    num_arr = ["1924", "1231234", "4177252841"]
    k_arr = [2, 3, 4]
    for number, k in zip(num_arr, k_arr):
        print(solution(number, k))
