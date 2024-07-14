import matplotlib.pyplot as plt
import math as m

# Define the functions
log_n = lambda x: m.log(x, 2)
n = lambda x: x
n_log_n = lambda x: x * m.log(x, 2)
n_2 = lambda x: x * x
n_3 = lambda x: x ** 3
expo = lambda x: 2 ** x
fact = lambda x: m.factorial(x)

# Define the x-points
xpts = [x for x in range(1, 101, 10)]

# Plot each function with a label
plt.plot(xpts, [log_n(x) for x in xpts], label='log(n)')
plt.plot(xpts, [n(x) for x in xpts], label='n')
plt.plot(xpts, [n_log_n(x) for x in xpts], label='n log(n)')
plt.plot(xpts, [n_2(x) for x in xpts], label='n^2')
plt.plot(xpts, [n_3(x) for x in xpts], label='n^3')
plt.plot(xpts, [expo(x) for x in xpts], label='2^n')
plt.plot(xpts, [fact(x) for x in xpts], label='n!')

# Set the y-axis limit
plt.ylim([0, 1000])

# Add the legend
plt.legend(loc='upper right')

# Show the plot
plt.show()
