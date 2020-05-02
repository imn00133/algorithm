# https://leetcode.com/problems/diameter-of-binary-tree/
# Solved Date: 20.04.12.


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FastSolution:
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        self.ans = 1

        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.ans = max(self.ans, l+r+1)

        dfs(root)
        return self.ans - 1


class Solution:
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        if root:
            max_side_length, max_both_length = self.recursion_explore(root)
        else:
            max_both_length = 0
        return max_both_length

    def recursion_explore(self, root: TreeNode):
        if root.left is None and root.right is None:
            return 0, 0
        if root.left:
            left_length, left_max = self.recursion_explore(root.left)
            left_length += 1
        else:
            left_length, left_max = 0, 0
        if root.right:
            right_length, right_max = self.recursion_explore(root.right)
            right_length += 1
        else:
            right_length, right_max = 0, 0
        max_side_length = max(left_length, right_length)
        max_both_length = max(left_max, right_max, left_length + right_length)
        return max_side_length, max_both_length


def main():
    head = TreeNode(1)
    # head.right = TreeNode(3)
    head.left = TreeNode(2)
    # head.left.right = TreeNode(5)
    # head.left.left = TreeNode(4)
    print(Solution().diameter_of_binary_tree(head))


if __name__ == '__main__':
    main()
