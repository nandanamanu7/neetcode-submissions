import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]

        # Max heap the array stones (convert all vals to negative, heapify)
        heapq.heapify(stones)

        while (len(stones) >= 2):
            # Pop two largest vals
            s1 = -heapq.heappop(stones)

            s2 = -heapq.heappop(stones)

            # Compare, if not equal, add new value to heap
            if s1 != s2:
                # Max-Max2 if not equal
                newStone = s1 - s2
                heapq.heappush(stones, -newStone)

        # If a stone remains return it
        if stones:
            return -heapq.heappop(stones)
        
        else: 
            return 0        