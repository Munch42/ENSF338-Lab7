import random

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        self.balance = 0  # Initialize balance factor

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
            # Check if the new node is added to the shorter subtree of the pivot
            if (pivot.balance > 1 and data < pivot.left.data) or (pivot.balance < -1 and data > pivot.right.data):
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            else:
                print("Case 3 not supported")

# Test cases
tree = AVLTree()


tree.insert(10)  # Case 1: Pivot not detected
tree.insert(20)  # Case 1: Pivot not detected


tree.insert(30)  # Case 2: Pivot exists, shorter subtree


tree.insert(5)   # Case 1: Pivot not detected
tree.insert(15)  # Case 1: Pivot not detected

tree.insert(25)  # Case 2: Pivot exists, shorter subtree
tree.insert(12)  # Case 3: Unsupported case


tree.insert(35)  # Case 2: Pivot exists, shorter subtree