class Node(object):
    def __init__(self, root):
        self.left = None
        self.right = None
        self.root = root

    def insert(self, data):
        if self.root:
            if data < self.root:
                if not self.left:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.root:
                if not self.right:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.root = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.root)
        if self.right:
            self.right.printTree()


if __name__ == '__main__':
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    print(not root.printTree())
    print(not 'xx')
