class Node[T]:
    def __init__(self, data: T):
        self.data: T = data
    def setLeft(self, node: "Node[T]"):
        self.left = node
    def setRight(self, node: "Node[T]"):
        self.right = node
    def __repr__(self):
        return f"Node: {self.data}"

if __name__ == "__main__":
    parent: Node[str] = Node("klxcoder")
    print(parent)
    parent.setLeft(Node("klx"))
    parent.setRight(Node("coder"))
    print(parent.left)
    print(parent.right)