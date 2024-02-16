class Node:
    def __init__(self, data= None, next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        itr = self.head
        llstr = ''
        while itr: 
            suffix = ''
            if itr.next:
                suffix = '-->'
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)
if __name__ == "__main__":
        root = LinkedList()
        root.insert_at_begining(5)
        root.insert_at_begining(10)
        root.print()