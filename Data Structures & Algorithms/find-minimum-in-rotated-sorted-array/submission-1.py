class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1

        while (lo < hi):

            m = lo + (hi-lo) // 2

            if (nums[m] > nums[hi]):
                lo = m+1

            elif (nums[m] < nums[hi]):
                hi = m

        return nums[hi]