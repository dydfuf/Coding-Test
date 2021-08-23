def solution(numbers):
    answer = []
    for aNumber in numbers:
        temp = list('0'+bin(aNumber)[2:])
        if aNumber % 2 == 0:
            temp[-1] = "1"
        else:
            idx = "".join(temp).rfind("0")
            temp[idx] = "1"
            temp[idx+1] = "0"

        answer.append(int("".join(temp), 2))
    return answer


if __name__ == '__main__':
    print(solution([2, 7]), [3, 11])
