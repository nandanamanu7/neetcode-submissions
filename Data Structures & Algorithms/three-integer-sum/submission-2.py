class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trips = []

        nums.sort()


        # Fixed i 
        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i-1]):
                continue

            # two pointers est.
            left = i+1
            right = len(nums)-1

            while(left < right):
                val = nums[left] + nums[right] + nums[i]

                if (val < 0):
                    left += 1
                
                elif (val > 0):
                    right -= 1
                
                else:
                    trips.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while (left < right and nums[left] == nums[left-1]):
                        left += 1
        
        return trips

        
