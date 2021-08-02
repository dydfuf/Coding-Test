def move(dice, direction):
    if direction == 1:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]
        return dice
    elif direction == 2:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]
        return dice
    elif direction == 3:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]
        return dice
    else:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]
        return dice

if __name__ == "__main__":

    # input
    N, M, y, x, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    order = list(map(int, input().split()))

    dice = [0] * 7  # 주사위

    dy = [0, 0, 0, -1, 1]
    dx = [0, 1, -1, 0, 0]

    # 명령 수행
    for aOrder in order:
        if y + dy[aOrder] < 0 or y + dy[aOrder] >= N or x + dx[aOrder] < 0 or x + dx[aOrder] >= M:
            continue
        else:
            x, y = x + dx[aOrder], y + dy[aOrder]  # 좌표 이동
            dice = move(dice, aOrder)  # 주사위 이동

            if arr[y][x] == 0:
                arr[y][x] = dice[6]  # 주사위 -> 칸
            else:
                dice[6] = arr[y][x]  # 칸 -> 주사위
                arr[y][x] = 0  # 칸에 있는 수 0으로 수정

            print(dice[1])