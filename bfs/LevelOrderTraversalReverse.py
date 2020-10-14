from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


def reverse_level_order_traversal(node: TreeNode) -> list:
    traversed_list = []
    que = deque()
    cur_lvl = 0
    que.append((node, 0))
    results = []

    while len(que):
        popped_node, popped_level = que.popleft()
        if popped_level > cur_lvl:
            traversed_list.append(list(results))
            results = []
            cur_lvl += 1
        results.append(popped_node.val)
        if popped_node.left:
            que.append((popped_node.left, cur_lvl + 1))
        if popped_node.right:
            que.append((popped_node.right, cur_lvl + 1))

    if len(results):
        traversed_list.append(results)

    return list(reversed(traversed_list))


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(reverse_level_order_traversal(root)))


if __name__ == "__main__":
    main()

