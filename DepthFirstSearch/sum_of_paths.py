
# In a tree where each node can be a digit (0-9) and root to leaf path form a number. Find the sum of all the numbers
# formed by the root to leaf paths.


from pythonProject.DepthFirstSearch.tree_node import TreeNode


def sum_of_paths(root):
    paths = []
    current_path = []

    def fill_paths(node):
        if not node:
            return

        current_path.append(str(node.data))
        if not node.left and not node.right:
            paths.append(list(current_path))
        fill_paths(node.left)
        fill_paths(node.right)
        current_path.pop()

    fill_paths(root)
    sum_numbers = 0
    for path in paths:
        number = int(''.join(path))
        sum_numbers += number
    return sum_numbers


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(sum_of_paths(root)))


