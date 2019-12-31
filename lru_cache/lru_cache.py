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
    
    def get(self, key):
        #TODO
        # get value from key from storage
        # move key value to end of cache
        # return value of key

        node = None # default node to none
        if self.storage.get(key, None) is not None: # if we have a key
            node = self.storage[key] # set node to keys value == node
            self.list.move_to_end(node) # move node to tail of cache
        return node.value if node is not None else None # if not none, return the value




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
        #TODO
        # if size == limit
        #   if the key is not in the storage
        #       delete the cache head and from stor
        #       add the key to storage
        #       add the to cache tail                          <-|
        #   if the key is in the storage                         |
        #       update the stor key-value                        | can be consolidated
        #       del the old value, add it to the tail in cache <-|

        # if maxed out
        if self.size == self.limit:
            if self.storage.get(key, None) is not None: # if we have a key in storage 
                self.list.delete(self.storage[key]) # delete from list
            else: # if we dont have a key - means we're adding a new key
                k,v = list(self.storage.keys()), list(self.storage.values()) # create lists
                del self.storage[k [ v.index( self.list.head ) ] ] # del key from storage
                self.list.remove_from_head() # del cache head
        
        self.list.add_to_tail(value)  # add to tail of cache
        self.storage[key] = self.list.tail # add new key value to stor   
        self.size = self.list.length #update length

