class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            d[n] = d.get(n, 0) + 1 
        

        for num, count in d.items():
            freq[count].append(num)
        
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if (len(res) >= k):
                    return res
