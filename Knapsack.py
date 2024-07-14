def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtracking to find the items included in the knapsack
    res = dp[n][capacity]
    w = capacity
    items_included = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == dp[i - 1][w]:
            continue
        else:
            items_included.append(i - 1)
            res = res - values[i - 1]
            w = w - weights[i - 1]

    return dp[n][capacity], items_included

def get_items_from_user():
    num_items = int(input("Enter the number of items: "))
    items = []
    weights = []
    values = []

    for i in range(num_items):
        item = input(f"Enter the name of item {i + 1}: ")
        weight = int(input(f"Enter the weight of {item}: "))
        value = int(input(f"Enter the value of {item}: "))
        items.append(item)
        weights.append(weight)
        values.append(value)

    return items, weights, values


def main():
    items, weights, values = get_items_from_user()
    capacity = int(input("Enter the capacity of the backpack (in kg): "))

    max_value, items_included_indices = knapsack(weights, values, capacity)

    print(f"The maximum value that can be carried is: {max_value}")
    print("Items included in the backpack:")
    for index in items_included_indices:
        print(f"{items[index]} (Weight: {weights[index]}, Value: {values[index]})")


if __name__ == "__main__":
    main()
