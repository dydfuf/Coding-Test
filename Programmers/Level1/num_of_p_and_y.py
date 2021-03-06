def solution(s):
    answer = True
    s = s.lower()
    num_p = 0
    num_y = 0
    for i in s:
        if i == "p":
            num_p += 1
        if i == "y":
            num_y += 1

    return num_p == num_y

if __name__ == "__main__":
    s = "pPoooyY"
    print(solution(s))