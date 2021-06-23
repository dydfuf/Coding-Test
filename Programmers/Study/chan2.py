if __name__ == "__main__":
    input_str = input("문자열 입력 : ")

    first = []
    second = []
    third = []

    for i in range(1, len(input_str), 3):
        first.append(input_str[i])

    for i in range(0, len(input_str), 3):
        second.append(input_str[i])

    for i in range(2, len(input_str), 3):
        third.append(input_str[i])

    password = ''.join(first)
    password += ''.join(second)
    password += ''.join(third)
    print("=" * 20)
    print(password)