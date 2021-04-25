def compress(s, k):
    result = ""

    stack = [s[0:k]]
    nums = []
    count = 1
    for i in range(k, len(s) + 1, k):
        if stack[-1] == s[i:i + k]:
            count += 1
        else:
            stack.append(s[i:i + k])
            nums.append(count)
            count = 1
    if stack[-1] == '':
        stack.pop()

    for num, string in zip(nums, stack):
        if num == 1:
            result += string
        else:
            result += str(num) + string

    if len(nums) != len(stack):
        result += stack[-1]
    # print("stack", stack)
    # print("num", nums)
    return result


def solution(s):
    if len(s) == 1:
        return 1
    half_len = len(s) // 2

    result_set = []
    for i in range(1, half_len+1):
        result_set.append(len(compress(s, i)))

    # print(result_set)
    # print("min : ",min(result_set))
    return min(result_set)


if __name__ == "__main__":
    arr_s = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede",
             "abcabcabcabcdededededede", "xababcdcdababcdcd","a"]
    for s in arr_s:
        print(solution(s))
