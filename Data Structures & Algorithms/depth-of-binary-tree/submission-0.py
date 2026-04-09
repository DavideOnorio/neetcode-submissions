# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        queue = deque([root])
        depth = 0
        if root == None:
            return depth
        
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                
            depth += 1
            
        return depth
            

        