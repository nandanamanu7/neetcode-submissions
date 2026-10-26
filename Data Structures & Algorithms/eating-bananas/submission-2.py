class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Bin search for optimal value problem

        # Begins at the lowest possible (1)
        lo = 1
        # Up till the range of the max pile height
        hi = max(piles)

        # While within range
        while (lo < hi):
            # Possible k is probably around halfway
            k = (lo + hi) // 2


            hours = 0
            
            # Calculates total hours to eat all the piles
            for pile in piles:
                hours += math.ceil(pile/k)
            
            # If the total hours <= the h value, there may be a lesser value still able to beat this value, so we keep searching, but include the k in the range so we can come back

            if (hours <= h):
                hi = k
            
            # else, we set the lo to equal the new middle +1 to exclude the value from the range, since it is completely not working
            else:
                lo =k+1
        
        return lo

            