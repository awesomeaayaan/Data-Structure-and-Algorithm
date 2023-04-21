#finding the max value in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
    
    def find_max(self):
        if self.head is None:
            return None
        max_val = self.head.data
        current_node = self.head
        while current_node is not None:
            if current_node.data > max_val:
                max_val = current_node.data
            current_node = current_node.next
        return max_val

# Example usage:
ll = LinkedList()
ll.add_node(5)
ll.add_node(10)
ll.add_node(7)
ll.add_node(3)
max_val = ll.find_max()
print(max_val)  # Output: 10
