class Node:
    def __init__(self, dataval, next=None, prev=None):
        self.data = dataval
        self.next = next
        self.prev = prev

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def setPrev(self, prev):
        self.prev = prev

    def getPrev(self):
        return self.prev

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.length = 0

    def size(self):
        return self.length

    def add(self, dataval):
        new_node = Node(dataval)
        new_node.setNext(self.head)
        if self.head:
            self.head.setPrev(new_node)
        self.head = new_node
        self.length += 1

    def printList(self):
        res = []
        node = self.head
        while node:
            res.append(node.getData())
            node = node.next
        return res

bl = DoublyLinkedList(0)
bl.add(1)
bl.add(2)
print(bl.printList())





