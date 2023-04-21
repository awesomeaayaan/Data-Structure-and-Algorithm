#replace the max_value of the linked list with the given value
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
    
    def find_max_and_replace(self, value):
        if self.head is None:
            return None
        max_node = self.head
        current_node = self.head
        while current_node is not None:
            if current_node.data > max_node.data:
                max_node = current_node
            current_node = current_node.next
        max_node.data = value

# Example usage:
ll = LinkedList()
ll.add_node(5)
ll.add_node(10)
ll.add_node(7)
ll.add_node(3)
ll.find_max_and_replace(15)
current_node = ll.head
while current_node is not None:
    print(current_node.data)
    current_node = current_node.next
