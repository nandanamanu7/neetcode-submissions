class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = 0

        if (len(nums) < 1):
            return 0

        curr = 1

        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i-1] + 1):
                curr += 1
            elif (i > 0 and nums[i] == nums[i-1]):
                continue
            else:
                longest = max(longest, curr)
                curr = 1
        return max(longest, curr)
            
        