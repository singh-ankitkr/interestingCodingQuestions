from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(node: TreeNode) -> int:
    if not node:
        return -1

    que = deque()
    que.append((node, 0))

    while len(que):
        popped_node, popped_level = que.popleft()
        if not popped_node.left and not popped_node.right:
            return popped_level
        if popped_node.left:
            que.append((popped_node.left, popped_level + 1))
        if popped_node.right:
            que.append((popped_node.right, popped_level + 1))


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(min_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(min_depth(root)))


if __name__ == "__main__":
    main()
