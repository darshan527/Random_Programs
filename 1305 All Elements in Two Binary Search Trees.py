# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = []

    def dfs(self, root):
        if root == None:
            return
        self.res.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        self.res = []
        self.dfs(root1)
        self.dfs(root2)
        self.res.sort()
        return self.res