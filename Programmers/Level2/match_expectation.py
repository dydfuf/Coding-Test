"""
1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16
  1       2       3       4       5        6       7       8
      1               2                3                4
              1                                2

1번째 라운드에서 만나려면 차가 2^0
2번째 라운드에서 만나려면 차가


"""
def solution(n, a, b):
    _round = 0
    while True:
        a = (a//2) + (a%2)
        b = (b//2) + (b%2)
        _round += 1
        if a == b:
            break
    return _round


if __name__ == "__main__":
    print(solution(8, 4, 7), 3)
    print(solution(8, 4, 5), 3)

