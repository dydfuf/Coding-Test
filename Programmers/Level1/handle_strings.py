def solution(s):
    answer = True

    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i == "1" or i == "2" or i == "3" or i == "4" \
                    or i == "5" or i == "6" or i == "7" \
                    or i == "8" or i == "9" or i == "0":
                answer = True
            else:
                answer = False
                break
    else:
        return False

    return answer


if __name__ == "__main__":
    s = "a234"
    print(solution(s))
    s = "1234"
    print(solution(s))