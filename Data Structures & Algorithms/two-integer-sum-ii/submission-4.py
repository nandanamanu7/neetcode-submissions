class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # two pointers
        lo = 0
        hi = len(numbers)-1

        while (lo < hi):
            val = numbers[lo] + numbers[hi]
            if (val > target):
                hi -= 1
            elif (val < target):
                lo += 1
            else:
                return [lo+1, hi+1]


        