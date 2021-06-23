if __name__ == "__main__":
    arr = ["a", "e", "i", "o", "u"]

    sentence = "yesterday all my troubles seemed so far away"

    a = 0
    b = 0

    for alpha in sentence:
        if alpha in arr:
            b += 1
        else:
            if not alpha == " ":
                a += 1

    print("모음의 개수 : ", b)
    print("자음의 개수 : ", a)
