from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)

        for st in strs:
            lets = [0] * 26

            for s in st:
                lets[ord(s) - ord('a')] += 1
            
            a[tuple(lets)].append(st)
        
        return list(a.values())


            



        