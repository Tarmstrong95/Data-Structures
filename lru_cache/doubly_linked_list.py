"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def print(self):
        cur = self.head
        lis = '<- '
        if cur is not None:
            while cur.next is not None:
                lis += f'{cur.value} <-> '
                cur = cur.next
            lis += f'{cur.value} ->'
            print(lis)
        else: 
            print('List is empty')


    def add_to_head(self, value):
        """ functional """
        if self.head is None and self.tail is None:
            node = ListNode(value)
            self.head = node
            self.tail = self.head
        else:
            self.head.insert_before(value)
            if self.length < 2:
                self.tail = self.head
            self.head = self.head.prev
        self.length += 1

    def remove_from_head(self):
        """ functional """
        val = self.head.value
        if self.length < 2:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return val

    def add_to_tail(self, value):
        """ functional """
        if self.head is None and self.tail is None:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1

    def remove_from_tail(self):
        """ functional """
        val = self.tail.value
        if self.tail.prev is not None:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = None
            self.tail = None
        self.length -= 1
        return val

    def move_to_front(self, node):
        val = node.value
        if node is not self.head:
            if node is self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
            node.delete()
            self.length -= 1 # to handle add_to_head adding 1
            self.add_to_head(val)

    def move_to_end(self, node):
        val = node.value
        if node is not self.tail:
            if node is self.head:
                self.head = self.head.next
                self.head.prev = None
            node.delete()
            self.length -= 1 # to handle add_to_tail adding one
            self.add_to_tail(val)


    def delete(self, node):
        if self.length < 2:
            self.head = None
            self.tail = None
            self.length -= 1
        elif node is self.head:
            self.remove_from_head()
        elif node is self.tail:
            self.remove_from_tail()
        elif node is not self.head and node is not self.tail:
            node.delete()
            self.length -=1

    def get_max(self):
        max = 0
        cur = self.head
        if self.length < 1:
            return None
        elif self.length < 2:
            return self.head.value
        else:
            while cur.next is not None:
                if cur.value > max:
                    max = cur
                cur = cur.next
            if cur.value > max:
                max = cur.value
        return max

