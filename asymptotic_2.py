import matplotlib.pyplot as plt

# Define the functions
f = lambda n: 7 * n + 5
g = lambda n: n

# Define the constant c
c = 8

# Generate points for plotting
n_values = range(1, 101)

# Plot f(n) and c * g(n)
plt.plot(n_values, [f(n) for n in n_values], label='f(n) = 7n + 5')
plt.plot(n_values, [c * g(n) for n in n_values], label=f'c * g(n) = {c} * n')

# Mark the n0 value
plt.axvline(x=5, color='gray', linestyle='--', label='n0 = 5')

# Add labels and legend
plt.xlabel('n')
plt.ylabel('Value')
plt.ylim([0, 1000])
plt.legend(loc='upper left')

# Show the plot
plt.show()

# Generate table for n0, f(n), and c * g(n)
n_values_table = range(1, 11)
f_values_table = [f(n) for n in n_values_table]
c_g_values_table = [c * g(n) for n in n_values_table]

# Print the table
print("n0\tf(n)\tc * g(n)")
for n, f_val, c_g_val in zip(n_values_table, f_values_table, c_g_values_table):
    print(f"{n}\t{f_val}\t{c_g_val}")
