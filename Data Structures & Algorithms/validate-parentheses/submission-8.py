class Solution:
    def isValid(self, s: str) -> bool:
        openP = ["{", "(", "["]
        closedP = ["}", ")", "]"]
        stack = []

        for c in s:
            if c in openP:
                stack.append(c)

            elif c in closedP:
                if not stack or stack.pop() != openP[closedP.index(c)]:
                    return False

        if stack:
            return False

        return True 

