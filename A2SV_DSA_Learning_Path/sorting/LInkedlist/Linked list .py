class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    

class Linkelist:
    def __init__(self):
        self.head = None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count+= 1
            current = current.next
        
        
mylist = Linkelist()
print(mylist)