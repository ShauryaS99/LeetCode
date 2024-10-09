class Node:
    def __init__(self, key, val, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt
        
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.mru = Node(-1, -1)
        self.lru = Node(-1, -1)
        self.mru.next = self.lru
        self.lru.prev = self.mru

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        mru_node = Node(key, self.cache[key].val)
        self.del_node(self.cache[key])
        self.add_node(mru_node)
        self.cache[key] = mru_node
        return self.cache[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            mru_node = Node(key, value)
            self.del_node(self.cache[key])
            self.add_node(mru_node)
            self.cache[key] = mru_node
        else:
            if len(self.cache) == self.capacity:
                mru_node = Node(key, value)
                del self.cache[self.lru.prev.key]
                self.del_node(self.lru.prev)
                self.add_node(mru_node)
                self.cache[key] = mru_node
            else:
                mru_node = Node(key, value)
                self.add_node(mru_node)
                self.cache[key] = mru_node
                
    def add_node(self, node):
        old_mru = self.mru.next
        self.mru.next = node
        node.prev = self.mru
        node.next = old_mru
        old_mru.prev = node
    
    def del_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)