class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers) - 1
        while (lo < hi):
            n_h = numbers[hi]
            n_l = numbers[lo]
            if (n_h + n_l > target):
                hi -= 1
            elif (n_h + n_l < target):
                lo += 1
            else:
                return [1+lo, 1+hi]