def solution(nums):
    answer = 0
    set_nums = set(nums)
    if len(nums) // 2 < len(set_nums):
        answer = len(nums) // 2
    else:
        answer = len(set_nums)
    return answer


if __name__ == "__main__":
    nums = [3,3,3,2,2,4]
    print(solution(nums))
