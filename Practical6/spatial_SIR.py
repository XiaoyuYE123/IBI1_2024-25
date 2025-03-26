import numpy as np
import matplotlib.pyplot as plt
beta = 0.3
gamma = 0.05
timesteps = 100
size = 100
population = np.zeros((size, size))
outbreak = np.random.choice(range(size+1), 2)
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
    infected_coords = np.argwhere(population == 1)
    for x, y in infected_coords:
        # loop through the neighbors
        # for each neighbor, calculate the probability of infection
        # if the probability of infection is less than beta, infect the neighbor
        # if the probability of infection is less than gamma, recover the infected individual
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size:
                if population[nx, ny] == 0:
                    if np.random.rand() < beta:
                       new_population[nx, ny] = 1
                if np.random.rand() < gamma:
                    new_population[x, y] = 2
        population = new_population.copy()
    # plot the picture at some time steps
    if t in [1, 10, 30, 50, 100]:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.title(f't = {t}')
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.show()

    
 

