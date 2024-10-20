import numpy as np
import tkinter as tk
from tkinter import Canvas

# Simulation parameters
width, height = 200, 100  # Domain size
tau = 0.6  # Relaxation time
velocities = np.array([[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]])
weights = np.array([4 / 9] + [1 / 9] * 4 + [1 / 36] * 4)

# Initialize the fluid density and velocity distribution function
density = np.ones((height, width))
f = np.ones((height, width, 9)) * density[:, :, None] / 9
feq = np.copy(f)

# Boundary conditions (simple walls)
def apply_boundary_conditions(f):
    f[0, :, [2, 5, 6]] = f[0, :, [4, 7, 8]]  # Bounce-back at the top
    f[-1, :, [4, 7, 8]] = f[-1, :, [2, 5, 6]]  # Bounce-back at the bottom

def equilibrium(density, velocity):
    usqr = 3 / 2 * (velocity[..., 0] ** 2 + velocity[..., 1] ** 2)
    feq = np.zeros((height, width, 9))
    for i, v in enumerate(velocities):
        vu = 3 * (v[0] * velocity[..., 0] + v[1] * velocity[..., 1])
        feq[:, :, i] = density * weights[i] * (1 + vu + 0.5 * vu ** 2 - usqr)
    return feq

def velocity_to_color(velocity):
    """ Map velocity magnitude to color (blue for low, red for high). """
    magnitude = np.sqrt(velocity[..., 0] ** 2 + velocity[..., 1] ** 2)
    max_vel = np.max(magnitude)
    
    # Set minimum velocity for color scaling to prevent the whole field from being blue
    min_vel = 0.001  # Adjust as needed
    max_vel = max(max_vel, min_vel)
    
    colors = (magnitude / max_vel * 255).astype(np.uint8)
    return colors

# Add a larger initial velocity field for better visualization
def add_initial_velocity(velocity):
    """ Adds a strong velocity disturbance to the left side of the grid to simulate fluid inflow. """
    velocity[:, :10, 0] = 0.2  # Strong horizontal velocity on the left side
    velocity[:, :10, 1] = 0.0  # No vertical velocity initially

# Main simulation loop
def simulate(canvas, tk_root, steps=1000, delay=10):
    global f

    velocity = np.zeros((height, width, 2))  # Initialize velocity
    add_initial_velocity(velocity)  # Add strong initial velocity

    for step in range(steps):
        # Compute macroscopic quantities (density and velocity)
        density = np.sum(f, axis=2)
        velocity = np.zeros((height, width, 2))
        for i, v in enumerate(velocities):
            velocity[:, :, 0] += f[:, :, i] * v[0]
            velocity[:, :, 1] += f[:, :, i] * v[1]
        velocity /= density[:, :, None]

        # Collision step (relaxation towards equilibrium)
        feq = equilibrium(density, velocity)
        f += -(1 / tau) * (f - feq)

        # Apply boundary conditions
        apply_boundary_conditions(f)

        # Streaming step (move the particles to neighboring nodes)
        for i, v in enumerate(velocities):
            f[:, :, i] = np.roll(f[:, :, i], v, axis=(0, 1))

        # Update the canvas with velocity visualization
        colors = velocity_to_color(velocity)
        canvas.delete("all")  # Clear the canvas
        for y in range(height):
            for x in range(width):
                color_value = colors[y, x]
                color = f'#{color_value:02x}00{255 - color_value:02x}'  # Blue to Red gradient
                canvas.create_rectangle(x*5, y*5, (x+1)*5, (y+1)*5, outline=color, fill=color)

        # Pause before the next frame
        tk_root.update_idletasks()
        tk_root.update()
        canvas.after(delay)

# Create tkinter window
root = tk.Tk()
root.title("Fluid Simulation")
canvas_width, canvas_height = width * 5, height * 5  # Scale up for better visibility
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Start the simulation
simulate(canvas, root, steps=2000, delay=1)
root.mainloop()
