class Node(object):
    def __init__(self, dataVal = None, nextVal = None):
        self.dataVal = dataVal
        self.nextVal = nextVal


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def listPrint(self):
        node = self.head
        while node:
            print(node.dataVal)
            node = node.nextVal

    def insertAtBegin(self, data):
        if self.head:
            NewNode = Node(data)
            NewNode.nextVal = self.head
            self.head = NewNode
        else:
            self.head = Node(data)
        self.length += 1

    def insertAtEnd(self, data):
        node = Node(data)
        if self.head:
            temp = self.head
            while temp.nextVal:
                temp = temp.nextVal
            temp.nextVal = node
        else:
            self.head = node
        self.length += 1

    def insertAtMid(self, index, data):
        if index < 0 or index > self.length:
            print("error! index illegal!")
            return
        if index == 0:
            self.insertAtBegin(data)
        elif index == self.length - 1:
            self.insertAtEnd(data)
        else:
            j = 0
            temp = self.head
            prev = self.head
            node = Node(data)
            while temp.nextVal and j < index:
                prev = temp
                temp = temp.nextVal
                j += 1
            if j == index:
                node.nextVal = temp
                prev.nextVal = node

            self.length += 1


if __name__ == '__main__':
    l = LinkedList()
    l.head = Node(1)
    l.insertAtBegin(0)
    l.insertAtEnd(2)
    l.insertAtEnd(3)
    l.insertAtEnd(4)
    l.insertAtEnd(5)
    l.insertAtMid(3, 100)
    l.listPrint()
