# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Solved Date: 20.04.21.


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bst_from_preorder(self, preorder) -> TreeNode:
        root_node = TreeNode(preorder[0])
        for value in preorder:
            self.insert(root_node, value)
        return root_node

    def insert(self, root_node, value):
        if root_node.val < value:
            if root_node.right is None:
                root_node.right = TreeNode(value)
            else:
                self.insert(root_node.right, value)
        elif root_node.val > value:
            if root_node.left is None:
                root_node.left = TreeNode(value)
            else:
                self.insert(root_node.left, value)


def main():
    pass


if __name__ == '__main__':
    main()
