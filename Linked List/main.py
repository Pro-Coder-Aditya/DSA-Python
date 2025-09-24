class Node:
    def __init__(self, data):
        self.data = data  # store data
        self.next = None  # pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # initially empty list

    # Add a node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # if list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # traverse to the last node
            current = current.next
        current.next = new_node

    # Print the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

ll.display()  # Output: 10 -> 20 -> 30 -> None
