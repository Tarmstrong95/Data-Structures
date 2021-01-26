import sys
sys.path.append('/Users/tristonarmstrong/Documents/lambda/python/Data-Structures/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size = self.storage.length

    def pop(self):
        if self.size > 0:
            tmp = self.storage.remove_from_tail()
            self.size = self.storage.length
            return tmp
        else: 
            return None

    def len(self):
        return self.size
