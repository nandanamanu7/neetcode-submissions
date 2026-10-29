# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Check the edge case: no root exists
        if not root:
            return []

        # Declare a comprehensive q
        q = deque()

        # add the root value (1st level to the q)
        q.append(root)

        # declare result
        res = []


        # while q still exists 
        while q:
            # level and length of level
            level = []
            lenlev = len(q)

            for i in range(lenlev):
                node = q.popleft()

                level.append(node.val)

                if(node.left):
                    q.append(node.left)
                
                if(node.right):
                    q.append(node.right)

            res.append(level)

        return res
            

        

       
            
        