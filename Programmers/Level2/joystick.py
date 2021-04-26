def solution(name):
    answer = 0
    joys = "A" * len(name)
    count_arr = []
    zeros = 0
    for aName, aJoy in zip(name, joys):
        count = ord(aName) - ord(aJoy)
        if count == 0:
            zeros += 1
        if count > 13:
            count = 26 - count
        count_arr.append(count)

    # 0을 만나면 반대방향으로
    idx = 0
    while True:
        answer += count_arr[idx]
        count_arr[idx] = 0
        if sum(count_arr) == 0:
            break
        left, right = 1, 1
        while count_arr[idx - left] == 0:
            left += 1
        while count_arr[idx + right] == 0:
            right += 1
        if left < right:
            answer += left
            idx -= left
        else:
            answer += right
            idx += right

    return answer


if __name__ == "__main__":
    arr_name = [
        "JAZ",
        "JEROEN",
        "JAN",
    ]
    for name in arr_name:
        print(solution(name))

# abcdefghijklmnopqrstuvwxyz
