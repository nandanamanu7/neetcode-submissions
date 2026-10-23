class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lo = 0
        hi = lo
        seen = set()
        longest = 0

        while(hi < len(s)):
            while(s[hi] in seen):
                seen.remove(s[lo])
                lo += 1

            seen.add(s[hi])
            longest = max((hi-lo) + 1, longest)
            hi += 1
        return longest
                

       