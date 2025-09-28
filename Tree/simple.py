# Define a class for each node in the tree
class Node:
    def __init__(self, data):
        self.data = data        # store the node value
        self.children = []      # list to store child nodes

    # Method to add a child to the current node
    def add_child(self, child):
        self.children.append(child)

    # Method to display the tree structure
    def display(self, level=0):
        # Print the current node with indentation based on level
        print(" " * (level * 4) + str(self.data))
        # Recursively print all child nodes
        for child in self.children:
            child.display(level + 1)


# Create root node
root = Node("Root")

# Create child nodes
child1 = Node("Child1")
child2 = Node("Child2")
child3 = Node("Child3")

# Connect nodes
root.add_child(child1)      # Root → Child1
root.add_child(child2)      # Root → Child2
child1.add_child(child3)    # Child1 → Child3

# Display the tree
root.display()
