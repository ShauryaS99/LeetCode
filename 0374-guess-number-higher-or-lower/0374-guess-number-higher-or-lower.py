# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def binarySearch(low, high):
            mid = int((high - low) / 2) + low
            res = guess(mid)
            if res == 0:
                return mid
            # we guessed too low
            elif res == 1:
                return binarySearch(mid+1, high)
            # we guessed too high
            else:
                return binarySearch(low, mid-1)
        return binarySearch(1, n)