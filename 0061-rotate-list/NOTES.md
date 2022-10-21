Started off with a bruce force solution. A rotation of K places is equivalent to a rotation by 1, K times. 
Our intial solution was to iterate through the end of the LL (linked list), and shuffle the pointers so that there is 1 rotation. We call this method K times.
Obviously this is inefficient, and even resulted in a timeOut error in submissions. 
- Optimization: modulo the num_rotations by num_nodes. That way we don't do useless rotations. 
- This passed the submission but obviously we are running a max of N -1 rotations (each of which travels the length of the LL) resulting in ~ O(N^2)

An improvement is found by realizing a pattern. A rotation of K places is also equivalent to taking the LAST K Nodes and putting them in the beginning. To do this we must break the connection btwn the prev node, and point the end of the LL to the beginning. 
This results in a much faster runtime of O(n)
