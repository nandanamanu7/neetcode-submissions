class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        md = {}
        
        for m in magazine:
            md[m] = md.get(m, 0) + 1
        
        for r in ransomNote:
            if md.get(r, 0) == 0:
                return False
            md[r] = md.get(r, 0) - 1
        
        return True


        