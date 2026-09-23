class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        a = [[] for i in range(len(nums) + 1)]

        for n in nums:
            d[n] = d.get(n, 0) + 1 
        
        for n, c in d.items():
            a[c].append(n)
        
        sol = []
        
        for i in range(len(a) - 1, 0, -1):
            for n in a[i]:
                sol.append(n)
                if (len(sol) == k):
                    return sol