class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None
        
class DoublyLinkedList():
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    # this operation inserts items at the end of the linked list
    # so we have to manipulate the tail node in 0(1) running time
    
    def insert(self):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node