Diff from other traversals because of the avoidance of processing the root node until the right sub tree.

Pre: Root, left, right
Inorder: Left, Root, Right
Postorder: Left, Right Root

Somehow you need to avoid popping the root node until you have confirmed the right ​subtree has been processed. 
- Implement a visited set to make sure which nodes have been processed
- set curr=None after b/c we have exhausted the children and can wait to be popped up the above level
