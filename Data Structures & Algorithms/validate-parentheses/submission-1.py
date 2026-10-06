class Solution:
    def isValid(self, s: str) -> bool:
        o = ["(", "{", "["]
        c = [")", "}", "]"]
        st = []

        for i in s:
            if i in o:
                st.append(i)
            if i in c:
                if (len(st) == 0 or st.pop() != o[c.index(i)]):
                    return False
        
        return len(st) == 0

            

