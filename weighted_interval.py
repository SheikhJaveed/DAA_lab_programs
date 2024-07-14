def find_last_non_conflicting(intervals, n):
    for j in range(n - 1, -1, -1):
        if intervals[j][1] <= intervals[n][0]:
            return j
    return -1


def weighted_interval_scheduling(intervals):
    # Sort intervals by finish times
    intervals.sort(key=lambda x: x[1])

    n = len(intervals)

    # Initialize dp array where dp[i] represents the maximum profit up to the ith interval
    dp = [0] * n

    # Base case
    dp[0] = intervals[0][2]

    for i in range(1, n):
        # Include the current interval's profit
        incl_profit = intervals[i][2]
        l = find_last_non_conflicting(intervals, i)
        if l != -1:
            incl_profit += dp[l]

        # Store the maximum of including and not including the current interval
        dp[i] = max(incl_profit, dp[i - 1])

    return dp[-1]


def main():
    n = int(input("Enter the number of drama school requests: "))

    intervals = []
    print("Enter the requests with their start-time, finish-time, and amount (format: start finish amount):")
    for _ in range(n):
        start = int(input("Start time: "))
        finish = int(input("Finish time: "))
        amount = int(input("Amount: "))
        intervals.append((start, finish, amount))

    # Compute the maximum profit
    max_profit = weighted_interval_scheduling(intervals)

    print(f"Maximum profit: {max_profit}")


if __name__ == "__main__":
    main()
