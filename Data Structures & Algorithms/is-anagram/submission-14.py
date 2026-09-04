class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False

        sS, tS = {}, {}

        for i in range (len(s)):
            sS[s[i]] = 1 + sS.get(s[i], 0)
            tS[t[i]] = 1 + tS.get(t[i], 0)

        return tS == sS

            
        