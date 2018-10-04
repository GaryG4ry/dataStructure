# create a root
class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:   # if the root exist
            if self.data > data:    # inset data smaller than the root, we insert it into the left side
                if None == self.left:   # if the left side is not exist
                    self.left = Node(data)
                else:   # if the left side is exist
                    self.left.insert(data)  # insert the data to the left data
            elif self.data < data:  # same as insert data to the left side
                if None == self.right:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:   # if the root is not exist do:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def inorderTraversal(self, root):   # in-order traversal
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res


if __name__ == '__main__':
    root = Node(10)
    root.insert(11)
    root.insert(80)
    root.insert(8)
    root.insert(54)
    root.insert(1)
    print(root.inorderTraversal(root))