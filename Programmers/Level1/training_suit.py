def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)

    for aLost in new_lost:
        if aLost + 1 in new_reserve:
            new_reserve.remove(aLost + 1)
        elif aLost - 1 in new_reserve:
            new_reserve.remove(aLost - 1)
        else:
            n -= 1

    return n


if __name__ == "__main__":
    n = 5
    lost = [2, 4]
    reverse = [3]
    print(solution(n, lost, reverse))
