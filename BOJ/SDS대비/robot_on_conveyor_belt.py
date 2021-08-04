import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().split())
    belt = deque(map(int, input().split()))
    # 1은 올리는 위치, N은 내리는 위치
    isRobot = deque([False] * len(belt))


    # 회전
    # 로봇 이동
    # 로봇 올리기

    # 회전
    def rotate(isRobot, belt):
        isRobot.rotate(1)
        belt.rotate(1)

        # 로봇이 내리는 위치에 오면
        if isRobot[N - 1]:
            isRobot[N - 1] = False

        return isRobot, belt


    # 로봇 이동
    def move(isRobot, belt):
        temp = isRobot.copy()
        move_list = list()
        for i in range(N - 2, -1, -1):
            if belt[i + 1] >= 1 and not isRobot[i + 1] and isRobot[i]:
                isRobot[i + 1] = isRobot[i]
                isRobot[i] = False
                belt[i + 1] -= 1

        if belt[0] > 0 and not isRobot[0] and isRobot[len(isRobot) - 1]:
            isRobot[0] = temp[len(isRobot) - 1]
            belt[0] -= 1

        # 로봇이 내리는 위치에 오면
        if isRobot[N - 1]:
            isRobot[N - 1] = False

        return isRobot, belt


    # 로봇 올리기
    def put(isRobot, belt):
        if not belt[0] == 0:
            isRobot[0] = True
            belt[0] -= 1

        return isRobot, belt


    # 내구도가 0인 벨트 체크하기 @return 내구도가 0인 벨트의 수
    def checkValid(belt):
        count = 0
        for aBelt in belt:
            if aBelt == 0:
                count += 1

        return count


    result = 0
    while True:

        result += 1
        isRobot, belt = rotate(isRobot, belt)
        # print("Rotate", isRobot, belt)
        isRobot, belt = move(isRobot, belt)
        # print("Move", isRobot, belt)
        isRobot, belt = put(isRobot, belt)
        # print("Put", result, isRobot, belt)
        # print()
        if checkValid(belt) >= K:
            print(result)
            break
