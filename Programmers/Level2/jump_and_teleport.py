def solution(n):
    ans = 0

    while n > 0:
        if n % 2:
            ans += 1
        n //= 2

    return ans

# 1 => 1
# 2 => 1
# 3 => 2
# 4 => 1
# 5 => 1+4 => 2
# 6 => 4+2 => 2
# 5000 => 2500 1250 625

if __name__ == '__main__':
    arr_n = [5, 6, 5000]
    arr_result = [2, 2, 5]
    for n, result in zip(arr_n, arr_result):
        print(solution(n), result)
