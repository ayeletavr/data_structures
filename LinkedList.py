"""
author: ayelet.avraham@mail.huji.ac.il
"""

class Node:
    def __init__(self, data=None):
        """
        Constructor of node object.
        """
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self, head):
        """
        Constructor.
        """
        self.head = head

    def traverse(self):
        """
        Traverse the linked list.
        :return: last node.
        """
        currNode = self.head
        while currNode.next:
            currNode = currNode.next
        return currNode

    def insert(self, node):
        lastNode = self.traverse()
        lastNode.next = node

    def pop(self):
        toRemove = self.head
        prev = None
        while toRemove.next:
            prev = toRemove
            toRemove = toRemove.next
        returnNode = Node(toRemove)
        prev.next = None
        return returnNode

    def getIndex(self, data):
        currNode = self.head
        while currNode.next:
            if currNode.data == data:
                return currNode
            currNode = currNode.next
        return -1 # if node doesn't exist

    def getNodeByIndex(self, index):
        i = 0
        currNode = self.head
        while i < index:
            currNode = currNode.next
            i += 1
        return currNode

    def remove(self, index):
        i = 0
        toRemove = self.head
        prev = None
        while i < index:
            prev = toRemove
            toRemove = toRemove.next
            i += 1
        prev.next = toRemove.next

    def printList(self):
        curr = self.head
        while curr.next:
            print(curr.data)
            curr = curr.next
        print(curr.data)

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    myList = LinkedList(node1)
    myList.insert(node2)
    myList.insert(node3)
    myList.insert(node4)
    myList.printList()
    myList.pop()
    myList.printList()
    myList.remove(1)
    myList.printList()
