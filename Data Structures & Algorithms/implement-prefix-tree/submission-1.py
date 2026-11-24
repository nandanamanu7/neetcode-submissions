class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        # for each char in word
        for c in word:
            # if its not existing, add it
            if(c not in node.children):
                node.children[c] = TrieNode()
            
            # then continue down a level
            node = node.children[c]

        # Set the last node to end
        node.end = True 

    def search(self, word: str) -> bool:
        node = self.root

        for c in word:

            # doesn't exist 
            if (c not in node.children):
                return False 
            
            # moving down a level if exists
            node = node.children[c]
        
        return node.end


    def startsWith(self, prefix: str) -> bool:
        node = self.root 

        for c in prefix:
            if c not in node.children:
                return False
            
            node = node.children[c]
        
        return True
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False 