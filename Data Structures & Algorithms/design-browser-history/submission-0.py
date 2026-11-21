class BrowserHistory:

    def __init__(self, homepage: str):
        self.bstack = []
        self.fstack = []
        
        self.bstack.append(homepage)
        

    def visit(self, url: str) -> None:
        self.fstack = []
        self.bstack.append(url)
        

    def back(self, steps: int) -> str:
        for s in range(min(steps, len(self.bstack)-1)):
            self.fstack.append(self.bstack.pop())
        return self.bstack[-1]
        

    def forward(self, steps: int) -> str:
        for s in range(min(steps, len(self.fstack))):
            self.bstack.append(self.fstack.pop())
        return self.bstack[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)