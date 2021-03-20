"""
author: ayelet.avraham@mail.huji.ac.il
"""
class Node:

    def __init__(self, data):
        """
        Constructor
        """
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BST:

    def __init__(self, node):
        """
        constructor
        """
        self.root = node

    def find(self, x, root):
        if not x:
            return "NOT FOUND"
        if root.data == x:
            return self.root
        if x > root.data:
            self.find(x, root.right)
        else:
            self.find(x, root.left)

    def find_min(self, node):
        if node.left:
            return self.find_min(node.left)
        return node

    def find_max(self, node):
        if node.right:
            return self.find_max(node.right)
        return node

    def successor(self, x):
        """
        Finds the minimal node in x.right subtree.
        """
        if x.right:
            return self.find_min(x.right)
        curr = x.parent
        while curr:
            if x != curr.right:
                break
            x = curr
            curr = curr.parent
        return curr

    def printBST(self):
        print(self.find_min(self.root).data)
        curr = self.successor(self.find_min(self.root))
        while self.successor(curr):
            print(curr.data)
            curr = self.successor(curr)
        print(curr.data)



    def insert(self, node):
        y = None
        x = self.root
        while x:
            y = x
            if node.data  <= x.data:
                x = x.left
            else:
                x = x.right
            node.parent = y
        if not y:
            self.root = node
        elif node.data <= y.data:
            y.left = node
        else:
            y.right = node

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    tree = BST(node3)
    tree.insert(node1)
    tree.insert(node2)
    tree.insert(node4)
    tree.printBST()
