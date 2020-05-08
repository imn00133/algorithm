# https://leetcode.com/problems/cousins-in-binary-tree
# Solved Date: 20.05.08.

import collections


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_cousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = collections.deque()
        # node, parent, depth
        queue.append((root, None, 0))
        find_depth = 0
        find_parent = None
        find_value = (x, y)
        while queue:
            node, parent, depth = queue.popleft()
            if node is None:
                continue
            queue.append((node.left, node, depth+1))
            queue.append((node.right, node, depth+1))
            if node.val in find_value:
                if find_depth:
                    if find_depth == depth and find_parent != parent:
                        return True
                    else:
                        return False
                else:
                    find_depth = depth
                    find_parent = parent


    def is_cousins_fast(self, root: TreeNode, x: int, y: int) -> bool:
        queue = collections.deque()
        queue.append((root, None))
        while queue:
            n = len(queue)
            found_parent = None
            found_one = False
            for _ in range(n):
                current_node, parent = queue.popleft()
                if current_node.val == x or current_node.val == y:
                    if not found_one:
                        found_one = True
                        found_parent = parent
                    else:
                        return parent != found_parent
                if current_node.right:
                    queue.append((current_node.right, current_node))
                if current_node.left:
                    queue.append((current_node.left, current_node))
        return False


def main():
    solution = Solution()
    root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
    print(solution.is_cousins_fast(root, 5, 4))
    root2 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))


if __name__ == '__main__':
    main()
