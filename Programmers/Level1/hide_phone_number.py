def solution(phone_number):
    answer = '*' * (len(phone_number)-4)
    answer += phone_number[len(phone_number)-4:]
    return answer


if __name__ == "__main__":
    for phone_number in ["01033334444", "027778888"]:
        print(solution(phone_number))