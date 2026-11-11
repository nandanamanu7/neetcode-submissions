# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    
        def dfs(node):
            # Check
            if not node:
                return 0
            
            # Mark and explore 
            return 1 + max(dfs(node.right), dfs(node.left))

        return dfs(root)
    



        