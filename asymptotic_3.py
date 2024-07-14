import matplotlib.pyplot as plt

# Define the functions
f = lambda n: 7 * n**2 + n + 5
g = lambda n: n**2

# Define the constants c1 and c2
c1 = 6
c2 = 8

n_values = range(1, 101)

# Plot f(n), c1 * g(n), and c2 * g(n)
plt.plot(n_values, [f(n) for n in n_values], label='f(n) = 7n^2 + n + 5')
plt.plot(n_values, [c1 * g(n) for n in n_values], label=f'c1 * g(n) = {c1} * n^2')
plt.plot(n_values, [c2 * g(n) for n in n_values], label=f'c2 * g(n) = {c2} * n^2')

# Determine the n0 value programmatically
n0 = next(n for n in n_values if c1 * g(n) <= f(n) <= c2 * g(n))

# Mark the n0 value
plt.axvline(x=n0, color='gray', linestyle='--', label=f'n0 = {n0}')

# Add labels and legend
plt.xlabel('n')
plt.ylabel('Value')
plt.legend(loc='upper left')

# Show the plot
plt.show()
n_val_table=range(1,11)
f_val_table=[f(n) for n in n_val_table]
c1_g_table=[c1*g(n) for n in n_val_table]
c2_g_table=[c2*g(n) for n in n_val_table]

print('n0\tf(n)\tc1*g(n)\tc2*g(n)')
for n,f_val,c1_g_val,c2_g_val in zip(n_val_table,f_val_table,c1_g_table,c2_g_table):
    print(f'{n}\t{f_val}\t{c1_g_val}\t{c2_g_val}')

