from itertools import product


def solution(user_id, banned_id):
    banDict = dict()
    for aBannedId in banned_id:
        for aUserId in user_id:
            valid = True
            for aCharUserId, aCharBannedId in zip(aUserId, aBannedId):
                if not valid:
                    break
                if aCharBannedId == "*":
                    continue
                if aCharUserId != aCharBannedId:
                    valid = False
            if valid and len(aBannedId) == len(aUserId):
                if aBannedId in banDict.keys():
                    banDict[aBannedId].add(aUserId)
                else:
                    banDict[aBannedId] = {aUserId}

    values = []

    for aBannedId in banned_id:
        values.append(list(banDict[aBannedId]))

    temp = []
    for aProduct in product(*values):
        length = len(aProduct)
        setPd = set(aProduct)
        if length != len(setPd):
            continue
        setPd = list(setPd)
        setPd.sort()
        if setPd in temp:
            continue
        else:
            temp.append(setPd)

    return len(temp)


if __name__ == "__main__":
    arr_userId = [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["frodo", "fradi", "crodo", "abc123", "frodoc"],
                  ["frodo", "fradi", "crodo", "abc123", "frodoc"]]
    arr_bannedId = [["fr*d*", "abc1**"], ["*rodo", "*rodo", "******"], ["fr*d*", "*rodo", "******", "******"]]
    arr_result = [2, 2, 3]
    for user_id, banned_id, result in zip(arr_userId, arr_bannedId, arr_result):
        print(solution(user_id, banned_id), result)
