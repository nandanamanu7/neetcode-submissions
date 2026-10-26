# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        
        # if no root exists, return an empty array
        if not root:
            return []
        
        # begin a queue with the root value
        q = deque([root])
        res = []

        # while there are still values in the tree 
        while q:
    
            level = []

            # Until the remaining q is iterated through
            for i in range(len(q)):
                # dequeue the first val from queue
                node = q.popleft()
                # add to the level
                level.append(node.val)
                
                # left to right (Level order)
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            # Since this is level order traversal, level appended to result
            res.append(level)

        return res

            
        