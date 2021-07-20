if __name__ == "__main__":
    mylist = list()

    menu = "*****************\n" \
           "1. 이름 추가\n" \
           "2. 이름 삭제\n" \
           "3. 이름 수정\n" \
           "4. 종료"

    while True:
        print(menu)
        input_menu = int(input("메뉴 선택 : "))
        if input_menu == 1:
            # 이름 추가
            name = input("이름 : ")
            if name in mylist:
                print("이미 있는 이름")
            else:
                mylist.append(name)
                print(mylist)
        elif input_menu == 2:
            # 이름 삭제
            name = input("이름 : ")
            if name in mylist:
                mylist.remove(name)
                print(mylist)
            else:
                print("해당 이름은 없음")
        elif input_menu == 3:
            # 이름 수정
            name = input("이름 : ")
            if name in mylist:
                new_name = input("새이름 : ")
                mylist.remove(name)
                mylist.append(new_name)
                print(mylist)
            else:
                print("해당 이름은 없음")
        elif input_menu == 4:
            break
        else:
            print("1~4번 사이의 번호를 입력해 주세요")
