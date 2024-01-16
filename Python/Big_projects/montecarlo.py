import random
import numpy as np
import matplotlib.pyplot as plt

# Function to estimate pi using the Monte Carlo method
def estimate_pi(n):
    count = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            count += 1
    return 4 * count / n

# Generate a list of sample sizes
sample_sizes = np.logspace(1, 7, num=50, dtype=int)

# Generate a list of estimates of pi for each sample size
pi_estimates = [estimate_pi(n) for n in sample_sizes]

# Plot how the estimate of pi converges to the true value as more points are generated
fig, ax = plt.subplots()
ax.plot(sample_sizes, pi_estimates, 'o-')
ax.axhline(np.pi, color='r', linestyle='--', label='True Value')
ax.set_xscale('log')
ax.set_xlabel('Number of Points')
ax.set_ylabel('Estimated Value of pi')
ax.set_title('Estimating pi using the Monte Carlo method')
ax.legend()
plt.show()