from difflib import ndiff
from functools import reduce
from itertools import combinations


def diffCount(str1, str2):
    diff_str = reduce(str.__add__, (ndiff(str1, str2)))
    return diff_str.count("+") + diff_str.count("-")


def splitEmail(str1):
    sp = str1.split("@")

    return sp[0], sp[1]


# True 유사, False 유사 X
def checkNick(str1, str2):
    if diffCount(str1, str2) < 3:
        return True
    return False


def checkEmail(email1, email2):
    userName1, serverName1 = splitEmail(email1)
    userName2, serverName2 = splitEmail(email2)

    if userName1 == userName2:
        return True

    if serverName1 == serverName2:
        if diffCount(userName1, userName2) == 1:
            return True

    return False


def solution(nicks, emails):

    length = len(nicks)

    temp = [i for i in range(length)]

    _list = [i for i in range(length)]
    for comb in combinations(temp, 2):

        if checkNick(nicks[comb[0]], nicks[comb[1]]) and checkEmail(emails[comb[0]], emails[comb[1]]):
            comb = list(comb)
            comb.sort()

            if _list[comb[0]] < _list[comb[1]]:
                _list[comb[1]] = _list[comb[0]]

    answer = set(_list)
    return len(answer)


if __name__ == '__main__':
    arr_nicks = [["imhero111", "moneyman", "hero111", "imher1111", "hro111", "mmoneyman", "moneymannnn"],
                 ["99police", "99poli44"], ["99polico", "99policd"]]
    arr_emails = [
        ["superman5@abcd.com", "batman432@korea.co.kr", "superman@abcd.com", "supertman5@abcd.com", "superman@erty.net",
         "batman42@korea.co.kr", "batman432@usa.com"], ["687ufq687@aaa.xx.yyy", "87ufq687@aaa.xx.yyy"],
        ["687ufq687@aaa.xx.yyy", "587ufq687@aaa.xx.yyy"]]
    arr_result = [3, 2, 2]

    for nicks, email, result in zip(arr_nicks, arr_emails, arr_result):
        print(solution(nicks, email), result)
