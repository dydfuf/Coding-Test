import sys

N = int(sys.stdin.readline())
tree = {}

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def preOrder(Node):
    print(Node.value, end="")
    if Node.left != '.':
        preOrder(tree[Node.left])
    if Node.right != '.':
        preOrder(tree[Node.right])

def inOrder(Node):
    if Node.left != '.':
        inOrder(tree[Node.left])
    print(Node.value, end="")
    if Node.right != '.':
        inOrder(tree[Node.right])

def postOrder(Node):
    if Node.left != '.':
        postOrder(tree[Node.left])
    if Node.right != '.':
        postOrder(tree[Node.right])
    print(Node.value, end="")

for _ in range(N):
    value, left, right = map(str, input().split())
    tree[value] = Node(value, left, right)

preOrder(tree['A'])
print()
inOrder(tree['A'])
print()
postOrder(tree['A'])