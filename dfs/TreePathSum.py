
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_path_sum(node, current_sum, required_sum):
    if not node:
        return False

    if not node.left and not node.right:
        if node.val == required_sum - current_sum:
            return True
        return False

    left_val = tree_path_sum(node.left, current_sum + node.val, required_sum)
    right_val = tree_path_sum(node.right, current_sum + node.val, required_sum)
    return left_val or right_val


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(tree_path_sum(root, 0, 23)))
    print("Tree has path: " + str(tree_path_sum(root, 0, 16)))


main()
