​The trick for this question is the constraints on HOW TO implement the solution.
1. Brute Force: O(n^2) solution where we have 2 FOR LOOPS and get the product of every element except the current index
2. Division: Get the product of the whole array and divide by current index

Rather, the solution is a slight variation of #2. Instead of getting the 1 product of the array, we will have 2 arrays of products. The prefix & postfix. 

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>PREfix:</strong> [1,1,2,6]
<strong>POSTfix:</strong> [24,12,4,1]
<strong>Output:</strong> [24,12,8,6]
</pre>

We run through the nums array once to create the prefix array (prefix array is the numbers multiplied before the curr index)
- prefix[i] = nums[i - 1] * prefix[i - 1]

Again for the postfix array (postfix array is the numbers multiplied after the curr index)
- postfix[i] = nums[i + 1] * postfix[i + 1]

And multiply these 2 numbers together. 

This solution is intuitive because we cannot have division yet we need some kind of accumulating product (so we dont have an n^2 runtime) Thus we create an array of accumulating products from either side. 
