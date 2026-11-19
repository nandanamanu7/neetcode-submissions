import heapq 
import math

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # res
        topk = [] 

        # iterate 
        for x, y in points:
            # distance formula
            d = math.sqrt((x*x) + (y*y))

            # push to heap
            heapq.heappush(topk, (-d, x,y))

            # if heap exceeds k, then pop useless vals until
            if(len(topk) > k):
                heapq.heappop(topk)
            
        # res
        return [[item[1], item[2]] for item in topk]

        