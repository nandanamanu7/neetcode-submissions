class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = len(s)-1
        j = 0
        while (j <= i):
            if not s[j].isalnum():
                j += 1 
                continue
            if not s[i].isalnum():
                i -= 1
                continue
            if (s[i].lower() != s[j].lower()):
                return False
            j += 1
            i -= 1     
        return True
        
        