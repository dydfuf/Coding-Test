def solution(n, times):
    answer = 0
    times.sort()
    maxTime = times[len(times) - 1] * n
    start = 1
    end = maxTime
    while start <= end:
        available = 0
        maxTime = (start + end) // 2
        for time in times:
            available += maxTime // time
            if available >= n: break

        if available >= n:
            end = maxTime - 1
            answer = maxTime

        elif available < n:
            start = maxTime + 1

    return answer


if __name__ == "__main__":
    n = 6
    times = [7, 10]
    print(solution(n, times))
