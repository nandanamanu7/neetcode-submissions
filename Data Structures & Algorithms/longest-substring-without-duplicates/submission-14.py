class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        lo = 0
        hi = 0
        longest = 0
        for l in s:
            if s[hi] in seen:
                longest = max(longest, hi - lo)
                while (s[hi] in seen):
                    seen.remove(s[lo])
                    lo += 1
            seen.add(s[hi])
            hi += 1
                    
        return max(longest, hi-lo)
                
                
            

