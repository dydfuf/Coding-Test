if __name__ == "__main__":
    stack = []
    for i in range(67):
        stack.append(i ** 3)

    for s in stack:
        if s % 67 == 27:
            print(s)

    print(stack)