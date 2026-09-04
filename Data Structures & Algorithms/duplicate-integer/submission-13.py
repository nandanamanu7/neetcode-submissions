class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if the length of a nums set 
        return len(set(nums)) < len(nums)
        