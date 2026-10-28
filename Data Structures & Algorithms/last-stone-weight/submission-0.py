import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]

        heapq.heapify(stones)

        last = 0

        while (len(stones) >= 2):

            s1 = -heapq.heappop(stones)

            s2 = -heapq.heappop(stones)

            if s1 != s2:
                newStone = s1 - s2
                heapq.heappush(stones, -newStone)

        if stones:
            return -heapq.heappop(stones)

        else: 
            return last        