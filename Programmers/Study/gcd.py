def gcd(x,y):
    if y == 0:
        return x
    return gcd(y, x%y)


def lcm(x,y):
    return x*y // gcd(x,y)


if __name__ == "__main__":
    int1 = int(input("정수 1 입력 : "))
    int2 = int(input("정수 2 입력 : "))
    _gcd = gcd(int1, int2)
    _lcm = lcm(int1, int2)

    print(str(int1) + "," + str(int2) + "의 최대공약수 : ", _gcd)
    print(str(int1) + "," + str(int2) + "의 최소공배수 : ", _lcm)