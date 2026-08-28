# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check(root):
            if root is None:
                return 0
            lefth=check(root.left)
            if lefth==-1:
                return -1
            righth=check(root.right)
            if righth==-1:
                return -1
            if abs((lefth-righth))>1:
                return -1
            return 1+max(lefth,righth)
        if check(root)!=-1: 
            return True
        else:
            return False
        