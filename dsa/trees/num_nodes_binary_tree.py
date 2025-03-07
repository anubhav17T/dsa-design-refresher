class RootNode:
    def __init__(self):
        self.root = None
    def count_nodes(self,node):
        if node is None:
            return 0
        print(node.data)
        return 1 + self.count_nodes(node=node.left) + self.count_nodes(node=node.right)

class BinaryTreeNodes:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


bt = RootNode()
bt.root = BinaryTreeNodes(data=1)
bt.root.left = BinaryTreeNodes(data=2)
bt.root.right = BinaryTreeNodes(data=3)
bt.root.left.left = BinaryTreeNodes(data=4)
bt.root.left.right = BinaryTreeNodes(data=5)
bt.root.right.left = BinaryTreeNodes(data=6)
bt.root.right.right = BinaryTreeNodes(data=7)


print(bt.count_nodes(node=bt.root))
