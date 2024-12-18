import numpy as np
import pygame
from pygame.locals import QUIT

class FluidSimulation:
    def __init__(self, width=800, height=600, grid_size=10):
        self.width = width
        self.height = height
        self.grid_size = grid_size
        
        # Number of grid cells in each dimension
        self.nx = width // grid_size
        self.ny = height // grid_size
        
        # Fluid density and velocity fields
        self.density = np.zeros((self.nx, self.ny))
        self.velocity_x = np.zeros((self.nx, self.ny))
        self.velocity_y = np.zeros((self.nx, self.ny))

        # Temporary arrays for fluid update
        self.density_new = np.zeros_like(self.density)
        self.velocity_x_new = np.zeros_like(self.velocity_x)
        self.velocity_y_new = np.zeros_like(self.velocity_y)
        
        # Initialize some initial density in the middle
        self.density[self.nx//3:2*self.nx//3, self.ny//3:2*self.ny//3] = 1.0
        
    def apply_boundary_conditions(self):
        """ Apply boundary conditions to the fluid grid """
        self.density[0, :] = self.density[1, :]
        self.density[-1, :] = self.density[-2, :]
        self.density[:, 0] = self.density[:, 1]
        self.density[:, -1] = self.density[:, -2]

        self.velocity_x[0, :] = -self.velocity_x[1, :]
        self.velocity_x[-1, :] = -self.velocity_x[-2, :]
        self.velocity_x[:, 0] = -self.velocity_x[:, 1]
        self.velocity_x[:, -1] = -self.velocity_x[:, -2]
        
        self.velocity_y[0, :] = -self.velocity_y[1, :]
        self.velocity_y[-1, :] = -self.velocity_y[-2, :]
        self.velocity_y[:, 0] = -self.velocity_y[:, 1]
        self.velocity_y[:, -1] = -self.velocity_y[:, -2]
        
    def advect(self, dt=0.1):
        """ Update fluid properties (density and velocity) by advection """
        for i in range(1, self.nx-1):
            for j in range(1, self.ny-1):
                # Velocity-based advection
                x, y = i - self.velocity_x[i, j] * dt, j - self.velocity_y[i, j] * dt
                
                # Linear interpolation for advection
                x = np.clip(x, 0, self.nx-1)
                y = np.clip(y, 0, self.ny-1)
                xi, yi = int(x), int(y)

                self.density_new[i, j] = self.density[xi, yi]
                self.velocity_x_new[i, j] = self.velocity_x[xi, yi]
                self.velocity_y_new[i, j] = self.velocity_y[xi, yi]

        self.density, self.density_new = self.density_new, self.density
        self.velocity_x, self.velocity_x_new = self.velocity_x_new, self.velocity_x
        self.velocity_y, self.velocity_y_new = self.velocity_y_new, self.velocity_y

    def update(self):
        """ Update the simulation step """
        self.apply_boundary_conditions()
        self.advect()

    def render(self, screen):
        """ Render the fluid simulation as colors on the screen """
        color_grid = np.zeros((self.nx, self.ny, 3), dtype=np.uint8)

        # Map density to a color (using a grayscale map)
        color_grid[:, :, 0] = np.clip(self.density * 255, 0, 255)  # Red channel
        color_grid[:, :, 1] = np.clip(self.density * 255, 0, 255)  # Green channel
        color_grid[:, :, 2] = np.clip(self.density * 255, 0, 255)  # Blue channel

        # Create a surface from the grid data and render it on the screen
        surf = pygame.surfarray.make_surface(np.transpose(color_grid, (1, 0, 2)))  # Transpose for proper orientation
        screen.blit(surf, (0, 0))

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    sim = FluidSimulation(grid_size=10)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        
        sim.update()  # Update the fluid simulation
        
        screen.fill((0, 0, 0))  # Clear the screen
        sim.render(screen)  # Render the simulation
        
        pygame.display.flip()
        clock.tick(60)  # 60 FPS
    
    pygame.quit()

if __name__ == "__main__":
    main()
