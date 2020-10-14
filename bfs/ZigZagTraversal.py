from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zig_zag_traversal(node: TreeNode) -> list:
    traversed_list = []
    que = deque()
    current_level = 0
    que.append((node, current_level))
    results = []

    while len(que):
        popped_node, popped_level = que.popleft()
        if popped_level > current_level:
            if current_level % 2:
                results.reverse()
            traversed_list.append(list(results))
            current_level += 1
            results = []
        results.append(popped_node.val)
        if popped_node.left:
            que.append((popped_node.left, current_level + 1))
        if popped_node.right:
            que.append((popped_node.right, current_level + 1))

    if results:
        if current_level % 2:
            results.reverse()
        traversed_list.append(results)
    return traversed_list


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(zig_zag_traversal(root)))


if __name__ == "__main__":
    main()
