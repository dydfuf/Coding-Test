if __name__ == "__main__":
    md = dict()
    for _ in range(5):
        name = input("상품명 : ")
        price = int(input("가  격 : "))
        md[name] = price

    total_price = 0
    print("-" * 30)
    while True:
        buy = input("구매할 상품 : ")
        if md.get(buy):
            total_price += md[buy]
        else:
            print(buy + " 은 없습니다!")
            break
    print("-" * 30)
    print("총 구매금액 : ", total_price)