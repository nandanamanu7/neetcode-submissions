from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            letters = [0] * 26
            for i in range(len(s)):
                letters[ord(s[i]) - ord('a')] += 1
            d[tuple(letters)].append(s)

        return list(d.values())


        
        

        