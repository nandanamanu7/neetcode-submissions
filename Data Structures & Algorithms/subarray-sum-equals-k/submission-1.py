class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Keeps track of total subarrays
        count = 0
        # Keeps track of current sum so far
        currSum = 0
        # Hashmap keeping track of prefixes and times they occur 
        prefixSums = {0 : 1}
        
        for num in nums:
            currSum += num

            if (currSum - k in prefixSums):
                count += prefixSums[currSum-k]

            prefixSums[currSum] = prefixSums.get(currSum, 0) + 1
        
        return count 

        