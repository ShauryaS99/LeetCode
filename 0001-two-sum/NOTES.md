we want to complete this in O(n) time. In order to do that we need a lookup of O(1) which is done in a hashmap. What are we looking for? The value... so the value: index.

Then when looping through the list: we calculate the diff and check if this exists in the hashmap!
One edgecase is when the target is 2x. Then the current value will check the diff which is its own value. This is an error b/c it should not duplicate entries. So we add an extra check.

A cleaner way to solve this problem is to simplify this into one loop and have the hashmap set at the end to prevent a number from using itself as the hashmap entry.​
