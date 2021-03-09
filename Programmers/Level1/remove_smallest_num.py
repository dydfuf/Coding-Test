def solution(arr):
    smallest = min(arr)

    for i in range(0, len(arr)):
        if arr[i] == smallest:
            arr.pop(i)
            break

    if len(arr) == 0:
        return [-1]
    return arr


if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    print(solution(arr))
    arr = [10]
    print(solution(arr))