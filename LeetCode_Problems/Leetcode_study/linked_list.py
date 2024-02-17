class Node:
    def __init__(self, data= None):
        self.data = data
        self.next = None

    def insert_at_begining(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self):
        
        
    def insertAtEnd(self):
        pass
    def remove_node(self):
        pass
    def sizeOfLL(self):
        pass
    def printLL(self):
        pass
            
if __name__ == "__main__":
        pass