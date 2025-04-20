class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head ==None
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count +=1 
            current = current.getNext()

        return count
    
    def viewList(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()

    def viewLastElement(self):
        current = self.head
        while current != None:
            if current.getNext() == None:
                return current.getData()
            else:
                current = current.getNext()

    def search(self ,item):
        current = self.head
        size = 0
        found = False
        while current != None and not found:
            size += 1
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
    
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    

mylist = UnorderedList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(5)
mylist.add(6)

# print(mylist.size())
# print(mylist.viewList())
# print(mylist.viewLastElement())
mylist.viewList()
print("-------------------------")
mylist.remove(3)
print("-------------------------")

mylist.viewList()
