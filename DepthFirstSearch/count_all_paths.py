
# Count all paths in a tree with nodes containing positive numbers,
# where the sum traversing downwards is equal to the given sum.\

from pythonProject.DepthFirstSearch.tree_node import TreeNode


paths = []
current_path = []


def get_all_paths(root):
    if not root:
        return
    current_path.append(root.data)
    if not root.left and not root.right:
        paths.append(list(current_path))

    get_all_paths(root.left)
    get_all_paths(root.right)
    current_path.pop()
    return


def num_of_req_sum_subarrays(path, req_sum):
    count = 0
    current_sum = 0
    left = 0
    for right in range(len(path)):
        current_sum += path[right]
        if current_sum == req_sum:
            count += 1
        while current_sum >= req_sum:
            current_sum -= path[left]
            left += 1
    return count


def find_all_paths_to_sum(root, req_sum):
    get_all_paths(root)
    count = 0
    for path in paths:
        count += num_of_req_sum_subarrays(path, req_sum)
    return count


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(find_all_paths_to_sum(root, 11)))


main()