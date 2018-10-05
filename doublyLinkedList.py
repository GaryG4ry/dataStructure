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

    # add element to the beginning of list
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
            node = node.getNext()
        return res

    def remove(self, dataval):
        node = self.head
        while node:
            if node.getData() == dataval:
                next = node.getNext()
                prev = node.getPrev()
                if next:
                    next.setPrev(prev)
                if prev:
                    prev.setNext(next)
                else:
                    self.head = node
                self.length -= 1
                return True
            else:
                node = node.getNext()
        return False

bl = DoublyLinkedList(0)
bl.add(1)
bl.add(2)
bl.add(3)
bl.remove(2)
bl.add(4)
print(bl.printList())





