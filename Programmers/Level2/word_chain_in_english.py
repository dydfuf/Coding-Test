def solution(n, words):
    answer = [0, 0]

    said = []
    people = [[] for _ in range(n)]

    for i in range(len(words)):
        turn = i % n
        # print(turn, words[i], said)
        # 말했던 단어 또말하기
        if words[i] in said:
            # print("했던말 또하기")
            answer = [turn+1, len(people[turn])+1]
            break

        # 말하는 단어가 이전에 말한 사람의 끝말잇기가 아닐 때
        if people[turn-1]:
            if words[i][0] != people[turn-1][-1][-1]:
                # print("끝말 잇기가 아님")
                answer = [turn+1, len(people[turn])+1]
                break
        said.append(words[i])
        people[turn].append(words[i])
    return answer


if __name__ == '__main__':
    arr_n = [3, 5, 2]
    arr_words = [["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"],
                 ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish",
                  "hang", "gather", "refer", "reference", "estimate", "executive"],
                 ["hello", "one", "even", "never", "now", "world", "draw"]]
    arr_result = [[3, 3], [0, 0], [1, 3]]
    for n, words, result in zip(arr_n, arr_words, arr_result):
        print(solution(n, words), result)
