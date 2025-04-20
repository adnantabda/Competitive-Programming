class Node:
    def __init__(self, data):
        self.data = None
        self.next = None


class UnorderedList:
    def __init__(self):
        self.head = None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
    

        