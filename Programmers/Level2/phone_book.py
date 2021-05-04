def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            for k in range(len(phone_book[i])):
                if not phone_book[i][k] == phone_book[j][k]:
                    break
            else:
                return False
    else:
        return True

def solution2(phone_book):

    phone_book = sorted(phone_book)
    
    for phone_number, otherPhoneNumber in zip(phone_book, phone_book[1:]):
        if otherPhoneNumber.startswith(phone_number):
            return False
    return True

if __name__ == "__main__":
    arr_phone_book = [
        ["119", "97674223", "1195524421"],
        ["123", "456", "789"],
        ["12", "123", "1235", "567", "88"]
    ]

    for phone_book in arr_phone_book:
        print(solution2(phone_book))
