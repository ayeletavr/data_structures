"""
author: ayelet.avraham@mail.huji.ac.il
"""

class Stack:

    def __init__(self, data):
        """
        Constructor
        """
        self.data = data
        self.pointer = data
        self.size = 1

    def pop(self):
        self.data = None
        self.size -= 1
        return self.pointer

    def push(self, data):
        self.pointer = data
        self.size += 1

    def size(self):
        return self.size

if __name__ == "__main__":
    stack = Stack(1)
    stack.push(4)
    print(stack.pop())
    print(stack.size)

