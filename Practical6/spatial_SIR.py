#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# define the infectious posibility and recovery possibility
beta = 0.3
gamma = 0.05
# define the number of timesteps, size of the population and the initial outbreak
timesteps = 100
size = 100
# create a two-dimensional array to represent the population
population = np.zeros((size, size))
# randomly select two coordinates in the population to start the outbreak
outbreak = np.random.choice(range(size+1), 2)
# plot the initial population with the outbreak
population[outbreak[0], outbreak[1]] = 1
plt.figure(figsize=(6,4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.show()
# define the neighbors who may be infected
# loop through the time
neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]   
for t in range(1, timesteps+1):
    # create a new population to store the update epidemic
    new_population = population.copy()
    # find the coordinates of the infected individuals
    infected_coords = np.argwhere(population == 1)
    for x, y in infected_coords:
        # check the neighbors of the infected individuals
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size:
                # if the neighbor is susceptible, infect it with probability beta
                if population[nx, ny] == 0:
                    if np.random.rand() < beta:
                       new_population[nx, ny] = 1
                # if the neighbor is infected, recover it with probability gamma
                if np.random.rand() < gamma:
                    new_population[x, y] = 2
    # update the population for the next timestep
        population = new_population.copy()
    # plot the picture at some time steps
    if t in [1, 10, 30, 50, 100]:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.title(f'timestep = {t}')
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.show()

    
 

