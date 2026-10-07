class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        o_freq = [[] for k in range(len(nums)+1)]
        res = []


        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for n, i in freq.items():
            o_freq[i].append(n)
        
        for i in range(len(o_freq)-1, -1, -1):
            for n in o_freq[i]:
                if (len(res) >= k):
                    break
                res.append(n)

        return res


        
        


        
        

            