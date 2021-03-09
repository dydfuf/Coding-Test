def solution(x):
    str_x = str(x)
    sum_of_digit = 0
    for c in str_x:
        sum_of_digit += int(c)

    if x % sum_of_digit == 0:
        return True

    return False


if __name__ == "__main__":
    for x in [10, 12, 11, 13]:
        print(solution(x))