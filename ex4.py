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
                return node
            node = node.parent
        return None

    def _left_rotate(self, x):
        y = x.right
        if y is None:
            return  # Nothing to rotate
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
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
        if x is None:
            return  # Nothing to rotate
        y.left = x.right
        if x.right:
            x.right.parent = y
        x.parent = y.parent
        if not y.parent:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
        self.update_balance(y)
        self.update_balance(x)

    def _lr_rotate(self, node):
        self._left_rotate(node.left)
        self._right_rotate(node)

    def _rl_rotate(self, node):
        self._right_rotate(node.right)
        self._left_rotate(node)

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
                if data > pivot.left.data:
                    print("Case #3b: adding a node to an inside subtree (LR Rotation)")
                    self._lr_rotate(pivot)
                elif data < pivot.left.data:
                    print("Case #3a: adding a node to an outside subtree")
                    self._right_rotate(pivot)
            elif pivot.balance < -1:
                if data > pivot.right.data:
                    print("Case #3b: adding a node to an inside subtree (RL Rotation)")
                    self._rl_rotate(pivot)
                elif data < pivot.right.data:
                    print("Case #3a: adding a node to an outside subtree")
                    self._right_rotate(pivot.right)
                    self._left_rotate(pivot)
            else:
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"{node.data} (balance: {node.balance})")
            self.inorder(node.right)

# Final test cases for Exercise 4

tree = AVLTree()

# Case 3b: Left-Right (LR Rotation)
tree.insert(30)
tree.insert(10)
tree.insert(20)  # Expected: Case #3b: adding a node to an inside subtree (LR Rotation)

# Case 3b: Right-Left (RL Rotation)
tree.insert(40)
tree.insert(50)
tree.insert(45)  # Expected: Case #3b: adding a node to an inside subtree (RL Rotation)
