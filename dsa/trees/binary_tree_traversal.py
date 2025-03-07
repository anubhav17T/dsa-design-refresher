class RootNode:
    def __init__(self):
        self.root = None

    def pre_order(self, node):
        if node is None:
            return 0
        print(node.data, end=" ")
        self.pre_order(node=node.left)
        self.pre_order(node=node.right)


    def in_order(self,node):
        if node is None:
            return
        self.in_order(node=node.left)
        print(node.data,end=" ")
        self.in_order(node=node.right)

class BinaryTreeNodes:
    def __init__(self,data):
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

bt.pre_order(node=bt.root)
print("----")
bt.in_order(node=bt.root)