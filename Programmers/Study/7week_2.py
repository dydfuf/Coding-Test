if __name__ == "__main__":

    line = input("출력 줄수 입력 : ")
    for n in range(1, int(line)+1):
        print(' '*(int(line)-n) + '*'*(2*n-1))

