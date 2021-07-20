num1 = int(input('정수1 입력: '))
num2 = int(input('정수2 입력: '))
num3 = int(input('정수3 입력: '))
num4 = int(input('정수4 입력: '))


def gcd(a, b, *values):
    stack = 0
    for i in range(1, a + 1):
        rem1 = a % i
        rem2 = b % i
        if rem1 == 0 and rem2 == 0:
            stack = i

    print(a, ',', b, '의 최대공약수: ', stack)

    for j in range(1, stack + 1):
        rem1 = a % j
        rem2 = b % j
        rem3 = values[0] % j
        if rem1 == 0 and rem2 == 0 and rem3 == 0:
            stack = j
    print(a, ',', b, ',', values[0], '의 최대공약수: ', stack)

    for l in range(1, stack + 1):
        rem1 = a % l
        rem2 = b % l
        rem3 = values[0] % l
        rem4 = values[1] % l
        if rem1 == 0 and rem2 == 0 and rem3 == 0 and rem4 == 0:
            stack = l
    print(a, ',', b, ',', values[0], ',', values[1], '의 최대공약수: ', stack)


gcd(num1, num2, num3, num4)
