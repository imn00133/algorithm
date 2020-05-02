# Solved Date: 20.05.01.


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_valid_sequence(self, root: TreeNode, arr: list[int]) -> bool:
        def dfs(node, arr, index=0):
            if len(arr) == index or node is None:
                return False
            if node.val != arr[index]:
                return False
            elif len(arr) - 1 == index and node.left is None and node.right is None:
                return True
            flag = dfs(node.left, arr, index+1)
            if flag:
                return flag
            return dfs(node.right, arr, index+1)

        return dfs(root, arr)
