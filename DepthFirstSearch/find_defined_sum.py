
# In a binary tree find the path from root to leaf with a given sum.


from tree_node import TreeNode
from copy import deepcopy
path = []
paths = []


def find_paths(node, target_sum):
    paths = []
    path = []

    def find_path(node, target_sum):
        if node is None:
            return False

        if node.data == target_sum and node.left is None and node.right is None:
            path.append(node)
            paths.append(deepcopy(path))
            path.pop()
            return

        path.append(node)
        find_path(node.left, target_sum - node.data)
        find_path(node.right, target_sum - node.data)
        path.pop()

    find_path(node, target_sum)
    return paths

def print_path(lst):
    for ls in lst:
        for node in ls:
            print(node.data)

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(print_path(find_paths(root, 23)))
    print(print_path(find_paths(root, 16)))

main()