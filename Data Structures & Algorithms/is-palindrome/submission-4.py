class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo = 0
        hi = len(s) - 1
        while(lo < hi):
            if not s[hi].isalnum():
                hi -= 1
            elif not s[lo].isalnum():
                lo += 1
            elif s[lo].lower() != s[hi].lower():
                return False
            else:
                hi -= 1
                lo += 1
        return True 