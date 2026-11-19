class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current = nums[0]
        freq = 1

        for num in nums[1:]:
            if num != current:
                freq -= 1
            
            else: 
                freq += 1
            
            if freq <= 0:
                current = num
                freq = 1

    
        return current

    

        