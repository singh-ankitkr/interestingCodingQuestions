from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root: TreeNode) -> list:
    traversed_list = []
    que = deque()
    que.append((root, 0))
    curr_height = 0
    results = []

    while len(que):
        popped_node, level = que.popleft()
        if curr_height < level:
            traversed_list.append(list(results))
            results = []
            curr_height += 1
        results.append(popped_node.val)

        if popped_node.left:
            que.append((popped_node.left, level + 1))
        if popped_node.right:
            que.append((popped_node.right, level + 1))

    if len(results):
        traversed_list.append(results)

    return traversed_list


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(level_order_traversal(root)))


if __name__ == "__main__":
    main()

