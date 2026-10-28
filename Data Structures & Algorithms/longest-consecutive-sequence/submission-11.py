class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        
        longest = 0
        numSet = set(nums)
        
        for num in numSet:
            if (num - 1 not in numSet):
                curr = 1

                while(num + curr in numSet):
                    curr += 1

                longest = max(longest, curr)

        return longest            
     