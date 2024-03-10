class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            height_left = height[left]
            height_right = height[right]
            curr_area = min(height_left, height_right) * (right-left)
            max_area = max(curr_area, max_area)
            if height_left < height_right:
                left += 1
            else:
                right -= 1
        return max_area