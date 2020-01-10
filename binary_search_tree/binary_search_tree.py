import sys
sys.path.append('/Users/tristonarmstrong/Documents/lambda/python/Data-Structures/queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        left = value < self.value
        right = value > self.value
        if left:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        elif right:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        left = target < self.value
        right = target > self.value
        match = target is self.value
        if match:
            return match
        else:
            if left:
                if self.left is not None:
                    return self.left.contains(target)
                else:
                    return match
            elif right:
                if self.right is not None:
                    return self.right.contains(target)
                else:
                    return match

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        left = self.left is not None
        right = self.right is not None
        cb(self.value)
        if left:
            self.left.for_each(cb)
        if right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #go left if can
        if node.left:
            self.in_order_print(node.left)
        #print root
        print(node.value)
        #go right if can
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = [node]
        curr = node
        while len(queue) > 0:
            curr = queue.pop(0)
            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)
            print(curr.value)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = [node]
        curr = node
        while len(stack) > 0:
            curr = stack.pop()
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            print(curr.value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass



# bst = BinarySearchTree(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)
# bst.bft_print(bst)