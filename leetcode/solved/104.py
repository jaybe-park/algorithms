# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find_depth(self, target_node):
        if target_node is None:
            return 0
        return max(self.find_depth(target_node.left), self.find_depth(target_node.right)) + 1
    
    def maxDepth(self, root: TreeNode) -> int:
        return self.find_depth(root)    
        