class Node:
    def __init__(self, key):
        self.key = key
        self.flag = False
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)
        self.count = 0

    def insert(self, string):
        cur = self.head

        for char in string:
            if char not in cur.children:
                cur.children[char] = Node(char)
            cur = cur.children[char]

        cur.flag = True

    def search(self, string):
        cur = self.head
        self.count = 0

        for char in string:
            if char not in cur.children:
                return False
            if cur.children.__len__() > 1:
                self.count = self.count + 1
            if cur.flag:
                self.count = self.count + 1

            cur = cur.children[char]

        if cur.flag:
            return True

        return False


# 4
# hello
# hell
# heaven
# goodbye
# 3
# hi
# he
# h
# 7
# structure
# structures
# ride
# riders
# stress
# solstice
# ridiculous
a = Trie()

a.insert("hello")
a.insert("hell")
a.insert("heaven")
a.insert("goodbye")

a.search("goodbye")
print(a.count)
