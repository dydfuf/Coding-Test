def solution(a, b):

    weeks = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    for i in range(0, a-1):
        day += days[i]
    day += b-1

    return weeks[day % 7]

if __name__ == "__main__":
    print(solution(1,2))