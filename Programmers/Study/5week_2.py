import datetime

if __name__ == "__main__":
    date = int(datetime.datetime.now().strftime('%d'))
    carNum = int(input("차량번호 입력 : "))

    # 짝수날
    if date % 2 == 0:
        if carNum % 2 == 0:
            print("오늘은 ", date, "로 짝수날로 주차 가능합니다.")
        else:
            print("오늘은 ", date, "로 짝수날로 주차 불가능합니다.")
    # 홀수 날
    else:
        if carNum % 2 == 0:
            print("오늘은 ", date, "로 홀수날로 주차 불가능 합니다.")
        else:
            print("오늘은 ", date, "로 홀수날로 주차 가능합니다.")