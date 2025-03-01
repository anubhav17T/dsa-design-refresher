""" Simple implementation of binary tree"""


class RootNode:
    def __init__(self):
        self.root = None

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.right, self.left = None, None

bt = RootNode()
bt.root = BinaryTreeNode(data=1)
bt.root.left = BinaryTreeNode(data=2)
bt.root.right = BinaryTreeNode(data=3)
bt.root.left.left = BinaryTreeNode(data=4)
bt.root.left.right = BinaryTreeNode(data=5)
bt.root.right.left = BinaryTreeNode(data=6)
bt.root.right.right = BinaryTreeNode(data=7)


