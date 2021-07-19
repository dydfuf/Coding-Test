import sys

N = int(sys.stdin.readline())

class Queue:
    def __init__(self):
        self.queue = list()

    def push(self, arg):
        self.queue.append(arg)

    def pop(self):
        if self.queue:
            result = self.queue.pop(0)
            return result
        else:
            return -1

    def size(self):
        return len(self.queue)

    def empty(self):
        if self.queue:
            return 0
        else:
            return 1

    def front(self):
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def back(self):
        if self.queue:
            return self.queue[-1]
        else:
            return -1


queue = Queue()
for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        queue.push(int(cmd[1]))
    elif cmd[0] == "pop":
        print(queue.pop())
    elif cmd[0] == "size":
        print(queue.size())
    elif cmd[0] == "empty":
        print(queue.empty())
    elif cmd[0] == "front":
        print(queue.front())
    elif cmd[0] == "back":
        print(queue.back())
    else:
        break