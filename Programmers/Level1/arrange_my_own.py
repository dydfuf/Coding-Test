def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])


if __name__ == "__main__":
    strings = ["sun", "bed", "car"]
    n = 1
    print(solution(strings, n))