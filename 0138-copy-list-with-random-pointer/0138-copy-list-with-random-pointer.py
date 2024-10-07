"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #O(n) for time and space
        if not head:
            return None
        
        # Intialize a dict of old_node => new_node
        # Used to check if new nodes have been copied or not
        # Must use old node as key b/c values can be duplicated!
        visited = {}
        visited[head] = Node(head.val)
        curr = head
        while curr:
            # Create curr.next in dict if doesn't exist
            if curr.next:
                if curr.next in visited:
                    visited[curr].next = visited[curr.next]
                else:
                    visited[curr.next] = Node(curr.next.val)
                    visited[curr].next = visited[curr.next]
            # Create curr.random in dict if doesn't exist
            if curr.random:
                if curr.random in visited:
                    visited[curr].random = visited[curr.random]
                else:
                    visited[curr.random] = Node(curr.random.val)
                    visited[curr].random = visited[curr.random]
                    
            curr = curr.next
        # Return value of head b/c this points to all the copied nodes
        return visited[head]
            
            
        