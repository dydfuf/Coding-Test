if __name__ == "__main__":
    password = "chan"

    for i in range(3):

        input_password = input("비밀번호 : ")
        if input_password == password:
            print("로그인 되었습니다!")
            break
        else:
            if i == 2:
                print("로그인 실패! 횟수 초과!")
                break
            print("비밀번호를 다시 입력하세요.")