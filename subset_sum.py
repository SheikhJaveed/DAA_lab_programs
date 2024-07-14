def subset_sum(set, sum):
    n = len(set)

    # Initialize the DP table
    dp = [[False] * (sum + 1) for _ in range(n + 1)]

    # Base case: A sum of 0 can always be achieved with an empty subset
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if set[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - set[i - 1]]

    # If the sum is not possible, return False
    if not dp[n][sum]:
        return False, []

    # Backtrack to find the subset
    subset = []
    i, j = n, sum
    while i > 0 and j > 0:
        if dp[i][j] and not dp[i - 1][j]:
            subset.append(set[i - 1])
            j -= set[i - 1]
        i -= 1

    return True, subset


def main():
    # Take user input for the set and the sum
    set_input = input("Enter the set of non-negative integers (comma separated): ")
    set_list = list(map(int, set_input.split(',')))
    sum_value = int(input("Enter the value of the sum: "))

    # Compute if there is a subset with the given sum
    result, subset = subset_sum(set_list, sum_value)

    if result:
        print(f"There is a subset of the given set with a sum equal to {sum_value}: {subset}")
    else:
        print(f"There is no subset of the given set with a sum equal to {sum_value}.")


if __name__ == "__main__":
    main()
