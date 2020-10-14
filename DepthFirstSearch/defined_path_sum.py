from pythonProject.DepthFirstSearch.tree_node import TreeNode


def all_paths_to_sum(root, number):
    paths = []
    current_path = []

    def path_to_sum(node, number):
        if not node:
            return

        current_path.append(node.data)
        if not node.left and not node.right:
            if node.data == number:
                paths.append(list(current_path))
                current_path.pop()
                return

        path_to_sum(node.left, number - node.data)
        path_to_sum(node.right, number - node.data)
        current_path.pop()

    path_to_sum(root, number)
    return paths


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(all_paths_to_sum(root, sum)))





