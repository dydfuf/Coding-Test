def solution(clothes):
    answer = {}

    for i in clothes:
        if i[1] in answer:
            answer[i[1]] += 1
        else:
            answer[i[1]] = 1


    temp = 1
    for i in answer.values():
        temp *= i+1
    return temp -1

if __name__ == '__main__':
    arr_clothes = [[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]], [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]]
    arr_answer = [5, 3]
    for clothes, answer in zip(arr_clothes, arr_answer):
        print(solution(clothes), answer)