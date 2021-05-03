def solution(record):
    answer = []
    user_list = dict()
    logs = [r.split(' ') for r in record]
    for aRecord in record:
        # check command
        split = aRecord.split(" ")
        command = split[0]
        userId = split[1]
        if command == "Enter":
            userNickname = split[2]
            user_list[userId] = userNickname
        elif command == "Change":
            userNickname = split[2]
            user_list[userId] = userNickname

    for aLog in logs:
        if aLog[0] == "Enter":
            answer.append(user_list[aLog[1]] + "님이 들어왔습니다.")
        elif aLog[0] == "Leave":
            answer.append(user_list[aLog[1]] + "님이 나갔습니다.")


    return answer


if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo",
              "Change uid4567 Ryan"]
    print(solution(record))
