
# Path with given sequence.
# Given a tree, find the path with given sequence from root to left.

from pythonProject.DepthFirstSearch.tree_node import TreeNode

current_path = []


def is_seq(root, seq, index):
    if not root:
        return False

    if index >= len(seq):
        return False

    current_path.append(root.data)
    if root.data != seq[index]:
        current_path.pop()
        return False
    else:
        if not root.left and not root.right:
            return True

    left_seq = is_seq(root.left, seq, index + 1)
    right_seq = is_seq(root.right, seq, index + 1)
    current_path.pop()
    if left_seq or right_seq:
        return True
    return False


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(is_seq(root, [1, 0, 7], 0)))
    print("Tree has path sequence: " + str(is_seq(root, [1, 1, 6], 0)))


