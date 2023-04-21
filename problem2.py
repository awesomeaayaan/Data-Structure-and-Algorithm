#Given a linked list containing whole numbers write a python function which finds and returns the sum of all the element at the odd position in the given linked list?
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
            
    def sum_odd_position(ll):
        if ll is None or ll.head is None:
            return 0
        current_node = ll.head
        sum_odd = 0
        index = 1
        while current_node is not None:
            if index % 2 != 0:
                sum_odd += current_node.data
            current_node = current_node.next
            index += 1
        return sum_odd

ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)
ll.add_node(5)

sum_odd = sum_odd_position(ll)
print(sum_odd)  # Output: 9 (1 + 3 + 5)
