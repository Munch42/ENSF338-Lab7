import random
import timeit
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

def insert(data, root=None):
    current = root
    parent = None
    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right
    
    if root is None:
        root = Node(data)
    elif data <= parent.data:
        parent.left = Node(data, parent)
    else:
        parent.right = Node(data, parent)
    return root

def search(root, data):
    current = root
    while current is not None:
        if current.data == data:
            return current
        elif data < current.data:
            current = current.left
        else:
            current = current.right
    return None

def height(node):
    # Base case: Height of empty tree is -1
    if node is None:
        return -1
    # Height = 1 + max of left height and right heights
    return 1 + max(height(node.left), height(node.right))

def balance_factor(node):
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    return left_height - right_height

# Function to find the maximum absolute balance factor in the entire tree. Helped by Claude
def max_balance_factor(root):
    if root is None:
        return 0
    
    # Compute balance factor for current node
    current_balance = abs(balance_factor(root))
    
    # Recursively find the maximum balance factor in left and right subtrees
    left_max = max_balance_factor(root.left)
    right_max = max_balance_factor(root.right)
    
    # Return the maximum of all three values
    return max(current_balance, left_max, right_max)

# Function to build a BST from a list of elements
def build_bst(elements):
    root = None
    for el in elements:
        if root is None:
            root = Node(el)
        else:
            root = insert(el, root)
    return root

numbers = list(range(0, 1000))
avgTimes = []
largestBalanceVals = []

for i in range(0, 1000):
    # Shuffled lists
    random.shuffle(numbers)
    tree = build_bst(numbers)
    
    listTimes = []
    # Find max balance factor across all nodes in the tree
    maxBalanceVal = max_balance_factor(tree)
    
    for j in range(0, 1000): 
        # Run for each task in each list
        timed = timeit.timeit(lambda: search(tree, numbers[j]), number=2) / 2
        listTimes.append(timed)
    
    avgTimes.append(sum(listTimes) / len(listTimes))
    largestBalanceVals.append(maxBalanceVal)

plt.figure(figsize=(12, 5))
plt.scatter(largestBalanceVals, avgTimes, s=10, label="BST Search", color="orange")
plt.xlabel("Maximum Absolute Balance Factor")
plt.ylabel("Search Times (s)")
plt.title("BST Search Times vs Maximum Absolute Balance Factor")
plt.legend()
plt.grid()
plt.show()