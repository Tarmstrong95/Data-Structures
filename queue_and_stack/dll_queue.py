import sys
sys.path.append('/Users/tristonarmstrong/Documents/lambda/python/Data-Structures/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList



class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size = self.storage.length

    def dequeue(self):
        if self.size > 0:
            tmp = self.storage.remove_from_tail()
            self.size = self.storage.length
            return tmp
        else:
            return None

    def len(self):
        return self.size
