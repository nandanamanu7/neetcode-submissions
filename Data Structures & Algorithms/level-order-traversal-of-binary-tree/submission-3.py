# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Address the edge case: no nodes exist
        if not root:
            return []

        # Declare a queue 
        q = deque()
        # Append the node to the queue
        q.append(root)
        result = []

        # As the queue exists
        while(q):
            # Declare an array for this level
            level = []
            # Take the current queue size
            levelSize = len(q)
            
            # iterate through the current level size
            for i in range(levelSize):
                # Add each of the nodes pushed into the queue onto level
                node = q.popleft()

                level.append(node.val)

                # If the node has any left or right children, append them to the queue in that order 
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            # Append this level to the result array
            result.append(level)
        
        return result




            

        

       
            
        