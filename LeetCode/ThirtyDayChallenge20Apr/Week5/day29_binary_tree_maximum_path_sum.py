# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Solved Date: 20.04.30.


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_path_sum(self, root: TreeNode) -> int:
        def explore_node(node):
            if node is None:
                return None, 0
            left_whole, left_value = explore_node(node.left)
            right_whole, right_value = explore_node(node.right)
            bigger_sum = max(left_value + node.val, right_value + node.val, node.val)
            if left_whole is None:
                left_whole = bigger_sum
            if right_whole is None:
                right_whole = bigger_sum
            whole_sum = max(left_whole, right_whole, bigger_sum, left_value + right_value + node.val)
            return whole_sum, bigger_sum

        return max(explore_node(root))


def main():
    # root = TreeNode(9, TreeNode(6), TreeNode(-3, TreeNode(-6), TreeNode(2, TreeNode(2, TreeNode(-6), TreeNode(-6)))))
    root = TreeNode(2, None, TreeNode(2, TreeNode(-6), TreeNode(-6)))
    solution = Solution()
    print(solution.max_path_sum(root))


if __name__ == '__main__':
    main()
