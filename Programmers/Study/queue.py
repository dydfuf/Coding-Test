if __name__ == "__main__":
    book_list = list()

    while True:
        menu = input("삽입/추출/종료 : ")

        if menu == "삽입":
            book_name = input("책 제목 : ")
            book_author = input("저자 : ")
            book_publisher = input("출판사 : ")
            book = [book_name, book_author, book_publisher]
            book_list.append(book)
        elif menu == "추출":
            if book_list:
                print(book_list.pop(0))
            else:
                print("자료가 없습니다.")
        elif menu == "종료":
            break
        else:
            print("삽입/추출/종료 중 하나를 선택해 주세요")