# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        from collections import deque
        queue = deque([root])

        while queue:
            node = queue.popleft()
            temp = None

            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        
        return root
        

        