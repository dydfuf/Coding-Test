from itertools import product

def solution(word):
    wordList = set()

    mo = ["A", "E", "I", "O", "U"]

    for i in range(1, 6):

        for j in product(mo, repeat=i):
            wordList.add("".join(j))

    wordList = list(wordList)
    wordList.sort()

    return wordList.index(word) + 1


if __name__ == '__main__':
    arr_word = ["AAAAE", "AAAE", "I", "EIO"]
    arr_result = [6, 10, 1563, 1189]
    for word, result in zip(arr_word, arr_result):
        print(solution(word), result)
