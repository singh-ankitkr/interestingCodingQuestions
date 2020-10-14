
# Find the max sum of a path in a tree.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindMaxSum:
    def __init__(self):
        self.max_sum = -100

    def get_path_sum(self, root):
        if not root:
            return 0

        left_path_sum = self.get_path_sum(root.left)
        right_path_sum = self.get_path_sum(root.right)
        path_sum = max(left_path_sum, right_path_sum) + root.val
        self.max_sum = max(self.max_sum, (left_path_sum + right_path_sum + root.val))
        return path_sum

    def get_max_path_sum(self, root):
        self.max_sum = 0
        self.get_path_sum(root)
        return self.max_sum


def main():
    maximumPathSum = FindMaxSum()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(maximumPathSum.get_max_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(maximumPathSum.get_max_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(maximumPathSum.get_max_path_sum(root)))


main()