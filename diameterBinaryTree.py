class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def depth(node):
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # Update the diameter
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            # Return the height of the current node
            return 1 + max(left_depth, right_depth)

        depth(root)
        return self.diameter

# Example Usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

solution = Solution()
print(solution.diameterOfBinaryTree(root))  # Output: 3
