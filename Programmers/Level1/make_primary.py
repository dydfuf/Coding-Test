def is_prime_num(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0

    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if is_prime_num(nums[i] + nums[j] + nums[k]):
                    answer += 1

    return answer


if __name__ == "__main__":
    nums = [[1, 2, 3, 4], [1, 2, 7, 6, 4]]
    for num in nums:
        print(solution(num))
