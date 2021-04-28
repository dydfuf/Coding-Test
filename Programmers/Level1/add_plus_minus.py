def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        if sign:
            answer += absolute
        else:
            answer += absolute*(-1)
    return answer

if __name__ == "__main__":
    arr_absolutes = [[4,7,12],
                     [1,2,3]]
    arr_signs = [[True,False,True],
                 [False,False,True]	]
    for absolutes, signs in zip(arr_absolutes, arr_signs):
        print(solution(absolutes, signs))