class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1

        while lo < hi:
            mid = lo + (hi-lo) // 2

            if (nums[mid] > nums[hi]):
                # Minimum must be to the right of mid
                lo = mid + 1
            else:
                # Mid could be the minimum, or minimum is to the left 
                hi = mid 
        
        return nums[lo]
