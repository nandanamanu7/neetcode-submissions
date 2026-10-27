class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0

        numSet = set(nums)
        longest = 1

        for num in nums:
            if (num-1 not in numSet):
                curr = 1
                while (num+curr in numSet):
                    curr += 1
                longest = max(curr, longest)

        return longest 
                
