class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if (target - nums[i]) in seen:
                return [min(seen.get(target-nums[i]), i), max(seen.get(target-nums[i]), i)]
            seen[nums[i]] = seen.get(nums[i], i)

    