At first glance we have a typical level order traversal where we can use BFS with a Queue to iterate through. We can use a simple while loop, appending the children to the queue while appending the values to a running list. 
HOWEVER,
We need to have each level in a separate list. This requires a small change. We need to break apart appending values to the result by 'LEVEL'. The queue will contain EXCLUSIVELY the next level AFTER the processing of the current level is completed. 
<pre>
                                                                                3
                                                                            /      \
                                                                           9       20
                                                                                  /   \      
                                                                                 15    7       
</pre>
<pre>
For instance, here after we finish the processing of 3, which entails:
1. Pop off the queue
2. Append the children to the queue
3. Append to the current level

We now have a clean slate for the next level. It is just the values in the Queue!
</pre>

So, if we take note of the length of the queue at this time we can pop off the exact number of elements that would be in the next level. Rinse and repeat.
Our solution has a simple while loop for the queue AND a for loop that iterates the exact number of elements that should be in the next level (the queue size before appending more children).
