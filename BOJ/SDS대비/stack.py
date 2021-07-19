import sys

N = int(sys.stdin.readline())

class Stack:

    def __init__(self):
        self.stack = list()

    def push(self, arg):
        self.stack.append(arg)

    def pop(self):
        if self.stack:
            top = self.stack.pop()
            return top
        else:
            return -1

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.stack:
            return 0
        else:
            return 1

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1


st = Stack()
for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        st.push(int(cmd[1]))
    elif cmd[0] == "pop":
        print(st.pop())
    elif cmd[0] == "size":
        print(st.size())
    elif cmd[0] == "empty":
        print(st.empty())
    elif cmd[0] == "top":
        print(st.top())
    else:
        break
