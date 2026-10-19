class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numstk = []

        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                op2 = numstk.pop()
                op1 = numstk.pop()
                if (t == "+"):
                    numstk.append(op1+op2)
                elif (t == "-"):
                    numstk.append(op1-op2)
                elif (t == "*"):
                    numstk.append(op1*op2)
                elif (t == "/"):
                    numstk.append(int(op1/op2))
            else:
                numstk.append(int(t))
            
        return numstk.pop()


