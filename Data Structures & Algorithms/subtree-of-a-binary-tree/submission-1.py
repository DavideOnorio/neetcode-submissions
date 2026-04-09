# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        from collections import deque
        
        def is_same(p,q):
            queue = [(p,q)]

            while queue:
                p,q = queue.pop(0)
                if p == None and q == None:
                    continue
                if q == None or p == None or q.val != p.val:
                    return False
                
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
                
            return True
        
        queue = deque([root])

        while queue:
            r = queue.popleft()

            if r.val == subRoot.val:
                if is_same(r,subRoot) == True:
                    return True
            if r.left != None:
                queue.append(r.left)
            if r.right != None:
                queue.append(r.right)
        
        return False
            
