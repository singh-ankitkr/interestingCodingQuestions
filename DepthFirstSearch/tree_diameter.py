
# Find the diameter of a tree.
diameter = 0


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_height(root):
    global diameter
    if not root:
        return 0

    left_height = get_height(root.left)
    right_height = get_height(root.right)
    height = max(left_height, right_height) + 1
    diameter = max(diameter, left_height + right_height + 1)
    return height


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    get_height(root)
    return diameter


print(main())
