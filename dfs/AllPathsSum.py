
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class AllPathsToSum:
    def __init__(self):
        self.all_paths = []
        self.current_path = []

    def all_paths_to_sum(self, node, current_sum, required_sum):
        if not node:
            return
        self.current_path.append(node.val)
        current_sum += node.val
        if not node.left and not node.right:
            if required_sum == current_sum:
                self.all_paths.append(list(self.current_path))

        self.all_paths_to_sum(node.left, current_sum, required_sum)
        self.all_paths_to_sum(node.right, current_sum, required_sum)
        self.current_path.pop()

    def execute(self, node, required_sum):
        self.all_paths_to_sum(node, 0, required_sum)
        return self.all_paths


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    required_sum = 23
    all_paths_obj = AllPathsToSum()
    print("Tree paths with required_sum " + str(required_sum) +
        ": " + str(all_paths_obj.execute(root, required_sum)))


main()
