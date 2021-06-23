def isMod3Eq0(x):
    return x % 3 == 0


if __name__ == "__main__":
    arr = []
    for _ in range(5):
        temp = int(input("정수 입력 : "))
        arr.append(temp)

    result_arr = list(filter(isMod3Eq0, arr))

    print("원본 리스트 : ", arr)
    print("결과 리스트 : ", result_arr)