class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lo = 0
        freq = {}
        longest = 0

        for hi in range(len(s)):
            freq[s[hi]] = freq.get(s[hi], 0) + 1

            while ((hi - lo + 1)- max(freq.values()) > k):
                freq[s[lo]] -= 1
                lo += 1
            
            longest = max(longest, hi-lo +1)

        return longest 


        