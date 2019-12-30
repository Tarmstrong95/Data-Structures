from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit #max cache size
        self.storage = {} #fast access to nodes
        self.size = 0 #size of cache list
        self.list = DoublyLinkedList() #cache


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    # what is "the order"
    # the value is the node
    # what is the point in having an LRU list as a storage dict and..
    # .. a LRU list in DLL format
    def get(self, key):
        # node default none
        node = None

        # traverse storage
        for keyi, val in self.storage.items():
            if keyi == key:
                node = val

        # if node is found
        if node is not None:
            del self.storage[key]
            self.storage.update({key: node})
        
        # return node as node or none
        return node

        #TODO
        # treverse storage for key
        # if found, copy key, del key, move key to end
        # if found, return value, else none



    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # node default to node or none
        node = self.get(key)

        # if node is found
        if node is not None:
            # del node from cache
            self.list.delete(node)
            # add node to tail of cache
            node.value = value
            self.list.add_to_tail(node.value)
        
        # if no node is found
        elif node is None:
            # check for size to limit
            if self.size == self.limit:
                # del head from cache and storage
                self.list.remove_from_head()
                del self.storage[list(self.storage.keys())[0]]

            # add node to tail of cache and storage
            self.list.add_to_tail(value)
            self.storage.update({key: self.list.tail})
            
        # update size to cache size
        self.size = self.list.length

        #TODO
        # if key exists in cache
            # move key value to end
        # else
            # check cache length, remove oldest if at max
            # add value to end

