So in this we use the classic slow vs fast pointer approach. it is important that the fast pointer starts one after the slow pointer. 

PATTERN:
1,2,3,4,5

slow = 1 -> 2 
fast = 2 -> 4

then increment slow once more 

1,2,3,4,5,6

slow = 1 -> 2 -> 3
fast = 2 -> 4 -> 6

then increment slow once more 
