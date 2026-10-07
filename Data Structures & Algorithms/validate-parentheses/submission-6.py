class Solution:
    def isValid(self, s: str) -> bool:
        o = ["(", "{", "["]
        c = [")", "}", "]"]

        stk = []

        for l in s:
            if l in o:
                stk.append(l)
            if l in c:
                if len(stk) == 0 or stk.pop() != o[c.index(l)]:
                    return False
        if len(stk) != 0:
            return False
        return True
