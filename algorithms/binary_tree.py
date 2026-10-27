NAME = "Binary Tree"
TYPE = "sort"


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                    return
                current = current.right

    def inorder(self):
        values = []

        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            values.append(node.value)
            traverse(node.right)

        traverse(self.root)
        return values


def run(numbers):
    steps = []
    tree = BinarySearchTree()
    data = list(numbers)

    for value in data:
        tree.insert(value)
        steps.append({
            "type": "compare",
            "index": value,
            "array": tree.inorder(),
        })

    if data:
        tree.root = None
        for value in data:
            tree.insert(value)
        tree.root = None
        steps.append({
            "type": "swap",
            "index1": 0,
            "index2": 0,
            "array": tree.inorder(),
        })

    steps.append({
        "type": "finished",
        "array": tree.inorder(),
    })

    return steps
