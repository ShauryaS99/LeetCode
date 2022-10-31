We must remove the nth node from the end of a Linked List. 

There are 2 approaches. Both run in O(n) but the first approach requires 2 passes of the Linked List.

The 'brute force' approach requires one additional piece of info: the size of the Linked List. This allows us to count from the beginning and not the end. That way when we get to the (size - n) Node, we know to skip it using a PREV_NODE variable.

The 1 PASS Solution has 2 pointers instead. One that is n spaces ahead of the first pointer. When this pointer reaches the end we know that our first pointer is n spaces from the end of the list (AS DESIRED). Here we follow the same process with the PREV_NODE variable


- The one edge case to watch out for is if we are removing the first node. In that case we just return head.next. This is difficult to deal with because there is not PREV_NODE to rely on since we are at the beginning of the list.
For CASE 1:
- Here since we know the size of the Linked List, we can easily tell if the value 'n' is telling us to delete the first node (n = size). 

For CASE 2:
- If our end pointer reaches the end of the list (NULL) we know that n was the size of the list. We know this because that is how many spaces the end pointer had to travel to get a headstart of value 'n' in front of our start pointer. 
