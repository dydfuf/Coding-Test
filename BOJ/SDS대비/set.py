import sys

input = sys.stdin.readline

if __name__ == "__main__":
    M = int(input())

    S = [False] * 20

    for _ in range(M):
        data = list(map(str, input().split()))

        cmd = data[0]
        param = 0
        if len(data) > 1:
            param = int(data[1]) - 1

        if cmd == "add":
            if not S[param]:
                S[param] = True
        elif cmd == "remove":
            if S[param]:
                S[param] = False
        elif cmd == "check":
            if S[param]:
                print(1)
            else:
                print(0)
        elif cmd == "toggle":
            if S[param]:
                S[param] = False
            else:
                S[param] = True
        elif cmd == "all":
            S = [True] * 20
        else:
            S = [False] * 20
