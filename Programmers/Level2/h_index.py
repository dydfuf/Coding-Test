def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for idx, i in enumerate(citations):
        if idx+1 <= i:
            answer = idx+1
    return answer

if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    answer = 3
    print(solution(citations), answer)
