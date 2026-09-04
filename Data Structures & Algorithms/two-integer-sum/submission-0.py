class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # key: num, val: index 

        for i, n in enumerate(nums):
            complement = target - n

            if complement in prevMap:
                return [prevMap[complement], i]

            prevMap[n] = i
            
        