import random
import timeit
import matplotlib.pyplot as plt

# Define the Node class for the BST
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right


# Function to insert a node into the BST
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


# Function to search for a value in the BST
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
    left_height = height(node.left)
    right_height = height(node.right)

    return left_height - right_height

# Function to build a BST from a list of elements
def build_bst(elements):
    root = None
    for el in elements:
        if root is None:
            root = Node(el)
        else:
            insert(el, root)
    return root

numbers = list(range(0, 1000))

avgTimes = []
largestBalanceVals = []
for i in range(0, 1000):
    # 1000 shuffled lists
    random.shuffle(numbers)
    tree = build_bst(numbers)

    listTimes = []
    maxBalanceVal = -1
    for j in range(0, 1000):
        # Run for each task in each list
        timed = timeit.timeit(lambda: search(tree, numbers[j]), number=10) / 10
        listTimes.append(timed)
        
        balFactor = abs(balance_factor(tree))
        if maxBalanceVal < balFactor:
            maxBalanceVal = balFactor

    avgTimes.append(sum(listTimes) / len(listTimes))
    largestBalanceVals.append(balFactor)

plt.figure(figsize=(12, 5))
plt.scatter(largestBalanceVals, avgTimes, s=10, label="BST Search", color="orange")
plt.xlabel("Absolute Balances")
plt.ylabel("Search Times (s)")
plt.title("Task Search Times of a BST vs Absolute Balances")
plt.legend()
plt.grid()

plt.show()