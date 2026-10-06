from collections import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        
        for s in strs:
            ltrs = [0] * 26
            for i in s:
                # incr pos by 1 
                ltrs[ord(i)-ord('a')] += 1 
            # for the letter config, append the anagram
            a[tuple(ltrs)].append(s)
        
        return list(a.values())
            



        