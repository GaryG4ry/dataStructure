# create a root
class BinaryTree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:  # if the root exist
            if self.data > data:  # inset data smaller than the root, we insert it into the left side
                if None == self.left:  # if the left side is not exist
                    self.left = BinaryTree(data)
                else:  # if the left side is exist
                    self.left.insert(data)  # insert the data to the left data
            elif self.data < data:  # same as insert data to the left side
                if None == self.right:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)
        else:  # if the root is not exist do:
            self.data = data

    # recursion
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    # recursion
    def inorderTraversal(self, root):  # in-order traversal    left->root->right
        res = []
        if root:    # once the node is not None
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def preorderTraversal(self, root):  # pre-order traversal   root->left->right
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res

    def postorderTraversal(self, root):  # post-order traversal  left->right->root
        res = []
        if root:
            res = res + self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res


if __name__ == '__main__':
    root = BinaryTree(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    print(root.printTree())
