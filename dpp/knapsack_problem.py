
# Items     -  ["Apple", "Orange", "Banana", "Melon"]
# Profits   -  [4, 5, 3, 7]
# Weights   -  [2, 3, 1, 4]
# Knapsack capacity - 5

# Find the max profit attainable (there is only one item each)


profits = [4, 5, 3, 7]
weights = [2, 3, 1, 4]
knapsack_capacity = 5


max_profit_arr = [[-1 for i in range(knapsack_capacity + 1)] for j in range(len(weights))]


# Recursive solution (O(2^n))
def max_profit(index, capacity):

    if index >= len(profits):
        return 0

    if max_profit_arr[index][capacity] != -1:
        return max_profit_arr[index][capacity]

    if weights[index] <= capacity:
        max_profit_arr[index][capacity] = max(max_profit(index + 1, capacity - weights[index]) + profits[index], max_profit(index + 1, capacity))

    else:
        max_profit_arr[index][capacity] = max_profit(index + 1, capacity)

    return max_profit_arr[index][capacity]


if __name__ == "__main__":
    print(max_profit(0, knapsack_capacity))
    print(max_profit_arr)