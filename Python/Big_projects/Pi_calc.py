import random
import matplotlib.pyplot as plt

def estimate_pi(num_points):
    inside_circle = 0
    
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []
    
    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x ** 2 + y ** 2
        
        if distance <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)
    
    pi_estimate = (inside_circle / num_points) * 4
    return pi_estimate, x_inside, y_inside, x_outside, y_outside

num_points = 1000000000
pi_estimate, x_inside, y_inside, x_outside, y_outside = estimate_pi(num_points)

print("Estimated π:", pi_estimate)

plt.figure(figsize=(6, 6))
plt.scatter(x_inside, y_inside, color='blue', label='Inside Circle')
plt.scatter(x_outside, y_outside, color='red', label='Outside Circle')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Estimating π using {num_points} points')
plt.legend()
plt.gca().add_artist(plt.Circle((0, 0), 1, color='black', fill=False))
plt.show()
