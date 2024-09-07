class Node:
    def __init__(self, key: int = -1, val: int = -1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # Intialize Doubly Linked List
        self.head = Node() # most recently used
        self.tail = Node() # least recently used
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.cache:
            #Update to MRU
            node = self.cache[key]
            self.delete_node(node)
            self.insert_mru_node(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Delete old node
            old_node = self.cache[key]
            self.delete_node(old_node)
            # Insert new node at MRU
            new_node = Node(key, value)
            self.insert_mru_node(new_node)
            self.cache[key] = new_node
        else:
            curr_size = len(self.cache)
            if curr_size == self.capacity:
                # Delete LRU node
                lru_node = self.tail.prev
                self.delete_node(lru_node)
                del self.cache[lru_node.key]
            # Insert new node at MRU
            new_node = Node(key, value)
            self.insert_mru_node(new_node)
            self.cache[key] = new_node
    
    # Insert most recent node after head
    def insert_mru_node(self, new_mru: Node):
        prev_mru = self.head.next
        # Update Head pointers
        self.head.next = new_mru
        # Update new mru pointers
        new_mru.next = prev_mru
        new_mru.prev = self.head
        # Update prev mru pointer
        prev_mru.prev = new_mru
        
    def delete_node(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)