class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
        self.balance = 0

class AVLTree:
    def __init__(self):
        self.root = None
    
    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def update_balance(self, node):
        if node:
            node.balance = self.height(node.left) - self.height(node.right)

    def find_pivot(self, node):
        while node:
            self.update_balance(node)
            if abs(node.balance) > 1:
                return node  # Pivot node detected
            node = node.parent
        return None  # No pivot detected

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        self.update_balance(x)
        self.update_balance(y)

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right is not None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
        self.update_balance(y)
        self.update_balance(x)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            print("Case #1: Pivot not detected")
            return

        current = self.root
        parent = None
        while current:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right

        new_node = Node(data, parent)
        if data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        pivot = self.find_pivot(new_node)
        if pivot is None:
            print("Case #1: Pivot not detected")
        else:
            self.update_balance(pivot)
            if pivot.balance > 1:
                if data < pivot.left.data:
                    print("Case #3b: not supported")
                elif data > pivot.left.data:
                    print("Case #3a: adding a node to an outside subtree")
                    self._left_rotate(pivot.left)
                    self._right_rotate(pivot)
            elif pivot.balance < -1:
                if data > pivot.right.data:
                    print("Case #3b: not supported")
                elif data < pivot.right.data:
                    print("Case #3a: adding a node to an outside subtree")
                    self._right_rotate(pivot.right)
                    self._left_rotate(pivot)
            else:
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")


# Test cases
tree = AVLTree()

tree.insert(10)  # Case 1: Pivot not detected
tree.insert(20)  # Case 1: Pivot not detected
tree.insert(30)  # Case 3b: not supported
tree.insert(5)   # Case 1: Pivot not detected
tree.insert(15)  # Case 1: Pivot not detected
tree.insert(25)  # Case 3b: not supported
tree.insert(12)  # Case 3a: adding a node to an outside subtree
tree.insert(35)  # Case 3b: not supported
tree.insert(40)  # Case 3b: not supported

