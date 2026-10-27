class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        m = 0
        while (right>left):
            new = min(heights[right], heights[left]) * (right-left)
            m = max(m, new)
            if (heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
        return m


        