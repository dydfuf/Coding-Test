if __name__ == "__main__":
    blood = list()
    for i in range(10):
        blood_type = input("헌혈할 혈액형 (a, b, ab, o) : ")
        blood.append(blood_type)

    print("저장된 혈액형")
    blood_a = blood.count("a")
    blood_b = blood.count("b")
    blood_ab = blood.count("ab")
    blood_o = blood.count("o")
    for _ in range(10):
        print(blood.pop(), end="")
        print("\t", end="")
    print("\nA 혈액형 수 : ", blood_a)
    print("B 혈액형 수 : ", blood_b)
    print("AB혈액형 수 : ", blood_ab)
    print("O 혈액형 수 : ", blood_o)
