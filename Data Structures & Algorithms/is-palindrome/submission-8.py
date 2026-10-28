class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo = 0
        hi = len(s)-1

        while (lo < hi):
            if not s[hi].isalnum():
                hi-=1
                continue
            elif not s[lo].isalnum():
                lo+=1
                continue
            elif s[hi].lower() != s[lo].lower():
                return False
            hi -= 1
            lo += 1
        
        return True