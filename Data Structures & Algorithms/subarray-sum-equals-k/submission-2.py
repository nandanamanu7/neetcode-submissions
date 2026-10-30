class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap = {0:1}
        currSum = 0
        count = 0

        for num in nums:
            # Add the current array value to currSum
            currSum += num 

            # Ask which old sum is necessary in order to make k 
            needed = currSum - k

            # Count how many times I saw it 
            count += prefixMap.get(needed, 0)

            # Remember the current sum and save to prefix map
            prefixMap[currSum] = prefixMap.get(currSum, 0) + 1
        
        return count


        