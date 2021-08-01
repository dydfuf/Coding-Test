def solution(s):
    answer = ''
    sp = s.split(" ")
    sp = list(map(int, sp))
    answer += str(min(sp)) + " " + str(max(sp))
    return answer

if __name__ == '__main__':
    arr_s = ["1 2 3 4"	, "-1 -2 -3 -4"	, "-1 -1"	]
    for s in arr_s:
        print(solution(s))
