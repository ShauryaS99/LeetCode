Approached it intuitively. 

I first got the order of letters from the first string. 
Then I got the frequency of those letters, plus the additional letters.
Then I iterated through the dict which was sorted based on order and created the new string. 

This would run in O(n) time.

Things to note: custom sorting on a dictionary.
sorted_dict = dict(sorted(alphabet_dict.items(), key=lambda x:x[1][0]))
​
How to get the lowercase alphabet (not used here but good to know)
import string
string.ascii_lowercase = 'abc....z'
