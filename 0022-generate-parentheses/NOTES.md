This is a backtracking question: essentially we are using recursion to iteratively build a set of all solutions. This contrasts from recursion slightly where we try to simplify it to a base case and bubble up.

In this question, we map out our state-space tree (a tree representing all states of the problem) AKA decision tree to try to find a pattern. 
<pre>
                                                                              n = 3
                                                                                (
                                                                            /      \
                                                                           (        )
                                                                         /   \      |
                                                                        (     )       (  
                                                                        |    / \     /   \
                                                                        )   (   )   (     )
</pre>
etc.
I found we have 1 rules for valid parantheses:
- At any given point: open_brackets >= closed_brackets

For building any combo we can break it down into a decision: OPEN_BRACKET VS CLOSED_BRACKET
There are 4 conditions I found for this decision
1. If there are 0 OPEN & 0 CLOSED: then return
2. If there are 0 OPEN & >0 closed: return )
3. There are EQUAL OPEN & CLOSED: return (
4. There are MORE OPEN THAN CLOSED: return either ( OR )

When we reach the base case we add it to the list and return
                                                                       
