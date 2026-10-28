class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        
        longest = 0
        numSet = set(nums)
        
        for i in range(len(nums)):
            if (nums[i] - 1 not in numSet):
                curr = 1

                while(nums[i] + curr in numSet):
                    curr += 1
                    
                longest = max(longest, curr)

        return longest            
     